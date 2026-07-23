class Garden:
    
    def __init__(self, diagram, students=None):
        self.row1, self.row2 = diagram.split("\n")
        
        if students is None:
            students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
                    "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
        students = sorted(students)
        self.students = students
        
    def plants(self, student):
        start = self.students.index(student) * 2
        row1plants = self.row1[start:start + 2]
        row2plants = self.row2[start:start + 2]
        plants = list(row1plants) + list(row2plants)
        plant_lookup = {
            "G": "Grass",
            "C": "Clover",
            "R": "Radishes",
            "V": "Violets"
            }
        fullnames = []
        for plant in plants:
            fullnames.append(plant_lookup.get(plant))
        return fullnames