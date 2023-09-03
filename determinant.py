class Determinant:
    def __init__(self):
        self.frames = {"Lotus": ["lotus", "лотус"],
                       "Eclipse": ["eclipse", "эклипс", "еклипс", "затмение"],
                       "Palefire": ["palefire", "палефайр", "палефаер", "пэйлфаер", "пэйлфайр", "бледный огонь"],
                       "Storm": ["storm", "шторм"],
                       "Dawn": ["dawn", "давн", "даун", "рассвет"],
                       "Lux": ["люкс", "lux"],
                       "Nightblade": ["nightblade", "найтблейд", "ночной меч", "ночной клинок"],
                       "Zero": ["zero", "зеро", "ноль", "нуль", "нулевая"],
                       "Blast": ["blast", "бласт", "взрыв"],
                       "Luminance": ["luminance", "люми", "люминанс", "яркость"],
                       "Entropy": ["entropy", "энтропи", "ентропи", "энтропия"],
                       "Ember": ["ember", "эмбер", "ембер", "уголёк", "уголек", "уголь"],
                       "Pulse": ["pulse", "пульс"],
                       "Tenebrion": ["tenebrion", "тенебрион"],
                       "Crimson Abyss": ["crymson abyss", "кримзон абисс", "багровая бездна",
                                         "алая бездна", "малиновая бездна"],
                       "Bastion": ["bastion", "бастион"],
                       "Astral": ["astral", "астрал"],
                       "Brilliance": ["brilliance", "бриллианс", "блеск"],
                       "Veritas": ["veritas", "веритас", "истина"],
                       "Silverfang": ["silverfang", "сильверфенг", "сильверфанг",
                                      "серебрянный клык", "sophia", "софия"],
                       "Arclight": ["arclight", "арклайт", "дуговой свет"],
                       "Plume": ["plume", "плюм", "перо"],
                       "Rozen": ["rozen", "розен"],
                       "Crocotta": ["camu", "каму", "crocotta", "крокотта"],
                       "Rigor": ["rigor", "ригор", "rosetta", "розетта"],
                       "Qilin": ["qilin", "changyu", "чангью", "цилин"],
                       "Pavo": ["qu", "pavo", "ку", "павлин", "паво"],
                       "Laurel": ["luna", "laurel", "луна", "лаурель", "лавр"],
                       "Hypnos": ["wanshi", "hypnos", "ванши", "гипноз"],
                       "Tempest": ["tempest", "темпест", "буря"],
                       "Glory": ["glory", "глори", "слава", "доблесть"],
                       "XXI": ["xxi", "21", "двадцать первая"],
                       "Garnet": ["garnet", "гарнет", "гранат"],
                       "Flambeau": ["roland", "flamebeau", "роланд", "пламя", "фламбо",
                                    "пламенный джентельмен", "пламенный кавалер"],
                       "Empyrea": ["empyrea", "эмпирея", "империя", "эмпайрея"],
                       "Capriccio": ["capriccio", "каприццио", "капучино"],
                       "Dragontoll": ["dragontoll", "драгонтолл", "налог дракона"],
                       "Starfarer": ["starfarer", "старфарер", "звёздный странник",
                                     "звездный странник"],
                       "Starveil": ["starveil", "старвейл", "звёздная вуаль",
                                    "звездная вуаль", "haicma", "хайкма"],
                       "Acire": ["scire", "скайр"],
                       "Arca": ["arca", "арка", "noan", "ноан", "shrek", "шрек"],
                       "Abystigma": ["abystigma", "абистигма", "balter", "alter",
                                     "бальтер", "альтер", "бездна"],
                       "Vitrum": ["bambinata", "vitrum", "витрум", "бамбината"],
                       "Hyperreal": ["hyperreal", "гиперреальность", "гиперреал"],
                       "Kaleido": ["kaleido", "калейдо"],
                       "Crimson Weave": ["crimson weave", "багровое переплетение",
                                         "алое переплетение", "малиновое переплетение"],
                       "Zitherwoe": ["zitherwoe", "зитервоу", "hanying", "ханьинг"],
                       "Feral Scent": ["feral scent", "ферал сент", "дикий запах"],
                       "Indomitus": ["indomitus", "noctis", "индомайтус", "индомитус", "неукротимый"],
                       "Echo": ["echo", "alisa", "эхо", "алиса"],
                       "Lost Lullaby": ["lamia", "lost lullany", "потерянная колыбель",
                                        "забытая колыбель", "потерянная колыбельная",
                                        "забытая колыбельная"]}
        self.frames_items = self.frames.items()
        self.names = {"Lucia": ["Lotus", "Dawn", "Plume", "Crimson Abyss", "Crimson Weave"],
                      "Lee": ["Palefire", "Entropy", "Hyperreal"],
                      "Liv": ["Eclipse", "Lux", "Luminance", "Empyrea"],
                      "Nanami": ["Storm", "Pulse", "Starfarer"],
                      "Kamui": ["Bastion", "Tenebrion"],
                      "Watanabe": ["Nightblade", "Astral"],
                      "Ayla": ["Brilliance", "Kaleido"],
                      "Bianca": ["Zero", "Veritas", "Abystigma"],
                      "Sophia": "Silverfang",
                      "Changyu": "Qilin",
                      "Chrome": ["Arclight", "Glory"],
                      "Vera": ["Rozen", "Farnet"],
                      "Camu": "Crocotta",
                      "Rozetta": "Rigor",
                      "Qu": "Pavo",
                      "Luna": "Laurel",
                      "Karenina": ["Blast", "Ember", "Scire"],
                      "Wanshi": "Hypnos",
                      "Selena": ["Tempest", "Capriccio"],
                      "Pulao": "Dragontoll",
                      "Haicma": "Starveil",
                      "Noan": "Arca",
                      "Bambinata": "Vitrum",
                      "Hanying": "Zitherwoe",
                      "No. 21": ["XXI", "Feral Scent"],
                      "Noctis": "Endomitus",
                      "Alisa": "Echo",
                      "Lamia": "Lost Lullany",
                      "Roland": "Flambeau"}
        self.names_items = self.names.items()

    def determination(self, frame):
        values = []
        myvalue = frame
        for key, value in self.frames_items:
            if myvalue in value:
                frame = str(key)
                values.append(frame)
                break
        for key2, value2 in self.names_items:
            if frame in value2:
                name = str(key2)
                values.append(name)
                break

        return values
