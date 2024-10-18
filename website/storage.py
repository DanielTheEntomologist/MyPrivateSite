"""Create a django storage class to interact with BunnyCDN storage API."""

from website.bunny_storage import Storage as BunnyStorage


from django.core.files.storage import Storage

from django.conf import settings

from django.core.files.base import File


class MyStorage(Storage):
    """Custom Storage class to interact with BunnyCDN storage API.

    methods:

    _open(name, mode='rb')
    Called by Storage.open(), this is the actual mechanism the storage class uses to open the file. This must return a File object,
    though in most cases, you’ll want to return some subclass here that implements logic specific to the backend storage system.
    The FileNotFoundError exception should be raised when a file doesn’t exist.

    _save(name, content)
    Called by Storage.save(). The name will already have gone through get_valid_name() and get_available_name(),
    and the content will be a File object itself.
    Should return the actual name of the file saved
    (usually the name passed in, but if the storage needs to change the file name return the new name instead).

    get_valid_name(name)
    Returns a filename suitable for use with the underlying storage system.
    The name argument passed to this method is either the original filename sent to the server or,
    if upload_to is a callable, the filename returned by that method after any path information is removed.
    Override this to customize how non-standard characters are converted to safe filenames.
    The code provided on Storage retains only alpha-numeric characters,
    periods and underscores from the original filename, removing everything else.

    get_alternative_name(file_root, file_ext)
    Returns an alternative filename based on the file_root and file_ext parameters.
    By default, an underscore plus a random 7 character alphanumeric string is appended to the filename before the extension.

    get_available_name(name, max_length=None)
    Returns a filename that is available in the storage mechanism, possibly taking the provided filename into account.
    The name argument passed to this method will have already cleaned to a filename valid for the storage system,
    according to the get_valid_name() method described above.
    The length of the filename will not exceed max_length, if provided.
    If a free unique filename cannot be found, a SuspiciousFileOperation exception is raised.
    If a file with name already exists, get_alternative_name() is called to obtain an alternative name.
    """

    def __init__(self, option=None):
        if not option:
            options = settings.CUSTOM_REMOTE_STORAGE_OPTIONS
        self.options = options
        self.storage = BunnyStorage(
            api_key=options["API_KEY"],
            storage_zone=options["STORAGE_ZONE"],
            storage_zone_region=options["STORAGE_ZONE_REGION"],
        )
        self.remote_storage_folder = options["FOLDER"]
        self.local_storage = settings.DEFAULT_FILE_STORAGE

    def _open(self, name, mode="rb"):
        """Open and return the file name."""
        name = name.replace("_", "-")
        name = name.replace(" ", "-")
        file = self.storage.DownloadFile(
            self.remote_storage_folder + "\\" + name, self.local_storage.path
        )
        return File(file, name)

    def get_valid_name(self, name: str) -> str:
        """Returns a filename suitable for use with the underlying storage system.
        The name argument passed to this method is either the original filename sent to the server or,
        if upload_to is a callable, the filename returned by that method after any path information is removed.
        Override this to customize how non-standard characters are converted to safe filenames.
        The code provided on Storage retains only alpha-numeric characters,
        periods and underscores from the original filename, removing everything else."""
        name = name.replace(" ", "-").replace("_", "-")
        return super().get_valid_name(name)

    def get_alternative_name(self, file_root, file_ext):
        return super().get_alternative_name(file_root, file_ext)

    def get_available_name(self, name, max_length=None):
        """Returns a filename that is available in the storage mechanism, possibly taking the provided filename into account.
        The name argument passed to this method will have already cleaned to a filename valid for the storage system,
        according to the get_valid_name() method described above.
        The length of the filename will not exceed max_length, if provided.
        If a free unique filename cannot be found, a SuspiciousFileOperation exception is raised.
        If a file with name already exists, get_alternative_name() is called to obtain an alternative name.
        """
        names_taken = self.storage.GetStoragedObjectsList(self.remote_storage_folder)
        names_taken = [name["File_Name"] for name in names_taken]
        print("Names taken: ", names_taken)
        if name in names_taken:
            name_core, name_ext = name.split(".")
            name_ext = "." + name_ext
            name = super().get_alternative_name(name_core, name_ext)
        return name

    def url(self, name):
        """Return the file url."""
        return f"https://borowiecki-personal-site.b-cdn.net/personal-site/{name}"

    def _save(
        self,
        name,
        content,
    ):
        """Save the file to the storage."""
        print("Saving file: ", name)
        print(
            "Content: ",
            content,
        )
        url = self.storage.PutFile(content, name, self.remote_storage_folder)
        return name
