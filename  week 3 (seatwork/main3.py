from pyscript import document
import random

def verify(event):
   
    registered = document.querySelector("#reg_status").checked
    medical = document.querySelector("#med_status").checked
    grade_str = document.querySelector("#grade_lvl").value
    section = document.querySelector("#section_val").value
    output = document.querySelector("#response-box")

   
    output.style.display = "block"
    output.className = ""
    
    if not grade_str or not section:
        output.classList.add("denied")
        output.innerHTML = "<strong>Incomplete:</strong> Please select your grade and section."
        return

    grade = int(grade_str)
    teams = ["Blue Bears", "Red Bulldogs", "Yellow Tigers", "Green Hornets"]
    
   
    instructions = []
    
    if not registered:
        instructions.append("Instruction: Please register online.")
    
    if not medical:
        instructions.append("Instruction: Please secure a medical clearance.")
        
    if not (7 <= grade <= 10):
        instructions.append("Instruction: Registration is only for Grades 7 to 10.")

  
    if not instructions:
        # ELIGIBLE
        my_team = random.choice(teams)
        output.classList.add("success")
        output.innerHTML = f"""
            <div style='font-size: 1.2rem; font-weight: bold;'>🎉 CONGRATULATIONS!</div>
            You are officially eligible to join.<br><br>
            <strong>TEAM:</strong> {my_team}<br>
            <strong>SECTION:</strong> {section} (Grade {grade})
        """
    else:
        # NOT ELIGIBLE
        output.classList.add("denied")
        error_msg = "<br>".join(instructions)
        output.innerHTML = f"<strong>NOT ELIGIBLE</strong><br>{error_msg}"
    
