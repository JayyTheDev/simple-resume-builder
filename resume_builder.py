def input_basic_info():
    print("=== Basic Info ===")
    name = input("Enter your full name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    return {"name": name, "email": email, "phone": phone}

def input_summary():
    print("\n=== Summary/Objective ===")
    summary = input("Write a short summary about yourself: ")
    return summary

def input_work_experience():
    print("\n=== Work Experience ===")
    experiences = []
    add_more = "y"
    while add_more.lower() == "y":
        job_title = input("Job Title: ")
        company = input("Company: ")
        start_date = input("Start Date (e.g., Jan 2020): ")
        end_date = input("End Date (or 'Present'): ")
        description = input("Description of your role/responsibilities: ")
        experiences.append({
            "job_title": job_title,
            "company": company,
            "start_date": start_date,
            "end_date": end_date,
            "description": description
        })
        add_more = input("Add another job? (y/n): ")
    return experiences

def input_education():
    print("\n=== Education ===")
    education_list = []
    add_more = "y"
    while add_more.lower() == "y":
        degree = input("Degree (e.g., BSc Computer Science): ")
        school = input("School/University: ")
        start_date = input("Start Date (e.g., Sep 2016): ")
        end_date = input("End Date (or 'Present'): ")
        education_list.append({
            "degree": degree,
            "school": school,
            "start_date": start_date,
            "end_date": end_date
        })
        add_more = input("Add another education entry? (y/n): ")
    return education_list

def input_skills():
    print("\n=== Skills ===")
    skills = input("Enter your skills, separated by commas: ")
    skill_list = [skill.strip() for skill in skills.split(",") if skill.strip()]
    return skill_list

def generate_resume(data):
    resume = f"""
{data['name']}
Email: {data['email']}
Phone: {data['phone']}

Summary:
{data['summary']}

Work Experience:
"""
    for job in data['work_experience']:
        resume += f"\n{job['job_title']} at {job['company']} ({job['start_date']} - {job['end_date']})\n"
        resume += f"{job['description']}\n"

    resume += "\nEducation:\n"
    for edu in data['education']:
        resume += f"\n{edu['degree']} from {edu['school']} ({edu['start_date']} - {edu['end_date']})\n"

    resume += "\nSkills:\n"
    resume += ", ".join(data['skills'])

    return resume

def main():
    print("Welcome to the Template-Based Resume Builder!\n")

    data = {}
    data.update(input_basic_info())
    data['summary'] = input_summary()
    data['work_experience'] = input_work_experience()
    data['education'] = input_education()
    data['skills'] = input_skills()

    print("\n\n===== Here is your generated resume =====\n")
    print(generate_resume(data))

if __name__ == "__main__":
    main()
