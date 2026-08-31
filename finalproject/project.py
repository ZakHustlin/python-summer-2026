import itertools
class Formula:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right
        
    def extract_variables(self):
        if self.left is None:
            return {self.right}
        else:
            return {self.left, self.right}

    def evaluate(self, truth):
        right_truth = truth[self.right]
        if self.left is None:
            return not right_truth

        left_truth = truth[self.left]
        

        if self.operator == "->":
            if left_truth and not right_truth:
                return False
            else:
                return True
        elif self.operator == "v":
            if left_truth or right_truth:
                return True
            else:
                return False
        elif self.operator == "^":
            if left_truth and right_truth:
                return True
            else:
                return False



def main():
    branch = input("Enter 'Truth Table Generation' or 'Proof Checker': ")
    if branch == "Truth Table Generation":
        formula = input("Enter a formula: ")
        parsed_formula = parse(formula)
        truth_table = build_truth_table(parsed_formula)
        classified_table = classify(truth_table)
        print(classified_table)
    elif branch == "Proof Checker":
        premise1 = input("Enter the first line of the proof: ")
        premise2 = input("Enter the second premise: ")
        conclusion = input("Enter the conclusion: ")
        parsed_p1 = parse(premise1)
        parsed_p2 = parse(premise2)
        parsed_c = parse(conclusion)
        if check_modus_ponens(parsed_p1, parsed_p2, parsed_c) == "Valid Modus Ponens":
            print("Valid Modus Ponens")
        elif check_modus_tollens(parsed_p1, parsed_p2, parsed_c) == "Valid Modus Tollens":
            print("Valid Modus Tollens")
        elif check_disjunctive_syllogism(parsed_p1, parsed_p2, parsed_c) == "Valid Disjunctive Syllogism":
            print("Valid Disjunctive Syllogism")
        else:
            print("No valid rule found")

    else:
        raise ValueError("Invalid Input")

def parse(formula_string):
    if "!" in formula_string:
        left = None
        operator = "!"
        right = formula_string.replace("!", "").strip()    
        return Formula(left, operator, right)
    elif " " in formula_string:
        left, operator, right = formula_string.split()
        return Formula(left, operator, right)
    else:
        return Formula(None, None, formula_string.strip())                
    

 

def generate_combinations(variables):
    values = []
    n = len(variables)
    items = itertools.product([True, False], repeat=n)
    for combo in items:
        values.append(dict(zip(variables, combo)))

    return values
    
          
   


def build_truth_table(formula):
    variables = formula.extract_variables()
    combinations = generate_combinations(variables)
    pairings = []
    for combo in combinations:
        pairing = (combo, formula.evaluate(combo))
        pairings.append(pairing)

    return pairings



def classify(results):
    truth = []
    for row in results:
        truth.append(row[1])
    if all(truth):
        return "tautology"
    elif not any(truth):
        return "contradiction"
    else:
        return "contingent"

    






def check_modus_tollens(premise1, premise2, conclusion):
    if premise1.operator == "->" and premise2.operator == "!" and premise2.right == premise1.right and conclusion.operator == "!" and conclusion.right == premise1.left:
        return "Valid Modus Tollens"
    else:
        return "Invalid Modus Tollens"


def check_modus_ponens(premise1, premise2, conclusion):
    if premise1.operator == "->" and premise1.left == premise2.right and conclusion.right == premise1.right:
            return "Valid Modus Ponens" 
    else:
        return "Invalid Modus Ponens"



def check_disjunctive_syllogism(premise1, premise2, conclusion):
    if premise1.operator == "v" and premise2.operator == "!" and premise2.right == premise1.left and conclusion.right == premise1.right:
        return "Valid Disjunctive Syllogism"
    else:
        return "Invalid Disjunctive Syllogism"



if __name__ == "__main__":
    main()  