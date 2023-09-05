import sqlite3


class Build():

    def __init__(self):
        self.builds = {"Main build": None,
                       "DPS Set": None,
                       "Elemental QTE": None,
                       "Physical QTE": None,
                       "QTE PPC": None,
                       "High Difficulty": None,
                       "Buff Set": None,
                       "High Rank": None}

    def build(self, frame):
        j = 0
        con = sqlite3.connect("frames.sqlite")
        cur = con.cursor()
        builds = cur.execute("""SELECT * FROM builds WHERE frame = ?""", (frame,)).fetchone()
        if builds:
            builds = [*builds]
            builds = builds[1:]
            for i in self.builds:
                self.builds[i] = builds[j]
                j += 1
            filtered = {k: v for k, v in self.builds.items() if v is not None}
            self.builds.clear()
            self.builds.update(filtered)
            return self.builds
        return
