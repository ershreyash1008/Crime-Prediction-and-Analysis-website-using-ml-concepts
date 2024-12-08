class Encodings:
    def state_values(state):
        if state == 'Alaska':
            return 1

        if state == 'Alabama':
            return 0

        if state == 'Arkansas':
            return 3

        if state == 'Arizona':
            return 2

        if state == 'California':
            return 4

        if state == 'Colorado':
            return 5

        if state == 'Connecticut':
            return 6

        if state == 'District of Columbia':
            return 8

        if state == 'Delaware':
            return 7

        if state == 'Florida':
            return 9

        if state == 'Georgia':
            return 10

        if state == 'Hawaii':
            return 11

        if state == 'Iowa':
            return 15

        if state == 'Idaho':
            return 12

        if state == 'Illinois':
            return 13

        if state == 'Indiana':
            return 14

        if state == 'Kansas':
            return 16

        if state == 'Kentucky':
            return 17

        if state == 'Louisiana':
            return 18

        if state == 'Massachusetts':
            return 21

        if state == 'Maryland':
            return 20

        if state == 'Maine':
            return 19

        if state == 'Michigan':
            return 22

        if state == 'Minnesota':
            return 23

        if state == 'Missouri':
            return 25

        if state == 'Mississippi':
            return 24

        if state == 'Montana':
            return 26

        if state == 'Nebraska':
            return 27

        if state == 'North Carolina':
            return 33

        if state == 'North Dakota':
            return 34

        if state == 'New Hampshire':
            return 29

        if state == 'Ohio':
            return 30

        if state == 'Oklahoma':
            return 31

        if state == 'Oregon':
            return 28

        if state == 'Pennsylvania':
            return 32

        if state == 'South Carolina':
            return 36

        if state == 'South Dakota':
            return 37

        if state == 'Tennessee':
            return 38

        if state == 'Texas':
            return 39

        if state == 'Utah':
            return 40

        if state == 'Virginia':
            return 41

        if state == 'Vermont':
            return 42

        if state == 'Washington':
            return 43

        if state == 'West Virginia':
            return 44

        if state == 'Wyoming':
            return 46

    def victim_sex(self):
        pass


    def weapons(weapon):
        if weapon=='Blunt Object':
            return 0

        if weapon=='Strangulation':
            return 13

        if weapon=='Unknown':
            return 15

        if weapon=='Rifle':
            return 11

        if weapon=='Knife':
            return 9

        if weapon=='Firearm':
            return 6

        if weapon=='Shotgun':
            return 12

        if weapon=='Fall':
            return 4

        if weapon=='Handgun':
            return 8

        if weapon=='Drowning':
            return 1

        if weapon=='Suffocation':
            return 14

        if weapon=='Explosives':
            return 3

        if weapon=='Fire':
            return 5

        if weapon=='Drugs':
            return 2

        if weapon=='Gun':
            return 7

        if weapon=='Poison':
            return 10

    def victim_sex(gender):
        if gender=='Male':
            return 1

        if gender=='Female':
            return 0

        if gender=='Unknown':
            return 2


    def victim_race(race):
        if race == 'Native American/Alaska Native':
            return 2

        if race == 'White':
            return 4

        if race == 'Black':
            return 1

        if race == 'Unknown':
            return 3

        if race == 'Asian/Pacific Islander':
            return 0

    def crime_type(crimeType):
        if crimeType=='Murder or Manslaughter':
            return 1

        if crimeType=='Manslaughter by Negligence':
            return 0



