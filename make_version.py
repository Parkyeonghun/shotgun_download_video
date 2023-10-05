import shotgun_api3

class MakeVersion:
    def __init__(self):
        SERVER_PATH = 'https://westrnd2.shotgrid.autodesk.com'
        SCRIPT_NAME = 'download_video'
        SCRIPT_KEY = '^trurx1vahkkezwyDotlzxvbs'

        self.sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)
    
    def create_shot(self):
        data = {
            'project': {"type":"Project","id": 122},
            'code': 'EW_TCC_0011',
            'description': 'Open on a beautiful field with fuzzy bunnies',
            'sg_status_list': 'ip'
        }

        self.sg.create('Shot', data)

    def create_version(self):
        data = {
            'project': {"type":"Project","id": 122},
            'code': 'EW_TCC_0011_v005',
            'sg_path_to_movie': "/home/t003/download/nature_-_31377 (1080p).mp4",
            'entity': {'type': 'Shot', 'id': 1207},
            'user': {'type': 'HumanUser', 'id': 88}
        }
        self.sg.create('Version', data)

    def upload_video(self):
        mp4 = "/home/t003/download/sea_-_4006 (540p).mp4"
        self.sg.upload("Version", 7028, mp4, field_name='sg_uploaded_movie')

        print(self.sg.find_one("Version", [["id", "is", 7027]], ['sg_uploaded_movie']))


if __name__ == "__main__":
    sp = ShotgunPractice()
    sp.upload_video()