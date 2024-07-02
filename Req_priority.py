class Requirements:
    def __str__(self):
        return f'{self.r_name}({self.DP})'
    
    def __init__(self, r_name, DP):
        self.r_name = r_name
        self.DP = DP
        self.parent = None
        self.childs = []

requirements_list = dict()

class RequirementManagement:
    def add_requirement(self, r_name, dp):
        r = Requirements(r_name, dp)
        requirements_list[r_name] = r
    
    def get_req(self, r_name):
        return requirements_list[r_name]
    
    def get_sorted_requirements(self):
        return sorted(requirements_list.values(), key=lambda r: r.DP, reverse=True)
    
    def print_sorted_requirements(self):
        sorted_requirements = self.get_sorted_requirements()
        for idx, req in enumerate(sorted_requirements, 1):
            print(f"{idx}. {req}")

    def print_top_10_requirements(self):
        sorted_requirements = self.get_sorted_requirements()[:10]
        for idx, req in enumerate(sorted_requirements, 1):
            print(f"{idx}. {req}")

def main():
    req_mgr = RequirementManagement()

    req_mgr.add_requirement('r1', 3)
    req_mgr.add_requirement('r2', 4)
    req_mgr.add_requirement('r3', 2.5)
    req_mgr.add_requirement('r4', 1.5)
    req_mgr.add_requirement('r5', 5.5)
    req_mgr.add_requirement('r6', 5)
    req_mgr.add_requirement('r7', 4.5)
    req_mgr.add_requirement('r8', 5.5)
    req_mgr.add_requirement('r9', 4)
    req_mgr.add_requirement('r10', 8)
    req_mgr.add_requirement('r11', 6.5)
    req_mgr.add_requirement('r12', 6.5)
    req_mgr.add_requirement('r13', 8)
    req_mgr.add_requirement('r14', 6.5)
    req_mgr.add_requirement('r15', 7)
    req_mgr.add_requirement('r16', 5)
    req_mgr.add_requirement('r17', 8)
    req_mgr.add_requirement('r18', 7)
    req_mgr.add_requirement('r19', 7)
    req_mgr.add_requirement('r20', 6.5)
    req_mgr.add_requirement('r21', 6)
    req_mgr.add_requirement('r22', 7)
    req_mgr.add_requirement('r23', 6)
    req_mgr.add_requirement('r24', 7)
    req_mgr.add_requirement('r25', 5.5)
    req_mgr.add_requirement('r26', 6.5)
    req_mgr.add_requirement('r27', 7)
    req_mgr.add_requirement('r28', 6)
    req_mgr.add_requirement('r29', 7)
    req_mgr.add_requirement('r30', 8)

    # Print top 10 sorted requirements with numbering
    #req_mgr.print_top_10_requirements()

    req_mgr.print_sorted_requirements()

if __name__ == "__main__":
    main()
