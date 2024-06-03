import json
import a_file


class ReadUserData:  # ReadUserData is called everytime any form is submitted on the site. It's a way to organize
    # the data of the patrons who visit & interact!
    def __init__(self, name, email, comments=None, like=None, dislike=None, album=None, song=None):
        self.name = name
        self.album = album
        self.song = song
        self.email = email
        self.comments = comments
        self.likes = like
        self.dislikes = dislike

    def __str__(self):
        return self.comments

    def displaying_data(self):  # this function would be used for my idea of another js feature: having an
        # animation on the homepage that displays comments made by a particular name. will continue to work on this
        # bc it'd be super cool but i'm having to teach myself js :)
        if self.likes is not None:
            return self.name + " said: " + self.likes

    def append_to_file(self):
        """
        uses json to append new data to data.json
        """
        with open('tests/data.json', 'r+') as f:
            data = json.load(f)
            data["critique_data"]["names"].append(self.name)
            data["critique_data"]["emails"].append(self.email)
            data["critique_data"]["comments"].append(self.comments)
            data["critique_data"]["likes"].append(self.likes)
            data["critique_data"]["dislikes"].append(self.dislikes)
            data["music_data"]["names"].append(self.name)
            data["music_data"]["albums"].append(self.album)
            data["music_data"]["songs"].append(self.song)
            f.seek(0)
            json.dump(data, f)
            f.truncate()


class SearchAndSort:
    @staticmethod
    def ic_email(e):
        return e.split('@')[1] == 'ithaca.edu'

    @staticmethod
    def search_for_ic_students():
        with open('tests/data.json', 'r') as f:
            data = json.load(f)
        email_list = data["critique_data"]["emails"]
        try:
            ic_students = filter(SearchAndSort.ic_email, email_list)
            return list(ic_students)
        except:
            a_list = []
            for email in email_list:
                if email is not None:
                    a_list.append(email)
            ic_students = filter(SearchAndSort.ic_email, a_list)
            return list(ic_students)


class SavingObjects:

    def write_to_file():
        """
        uses json to first create template in data.json
        """
        with open('tests/data.json', 'w') as f:
            data = {"critique_data": {"names": [],
                                      "emails": [],
                                      "comments": [],
                                      "likes": [],
                                      "dislikes": []
                                      },
                    "music_data": {"names": [],
                                   "albums": [],
                                   "songs": []
                                   }}

            json.dump(data, f)


def main():
    SavingObjects.write_to_file()


main()
