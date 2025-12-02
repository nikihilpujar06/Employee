from employee import employee_details 
def test_employee_details():
    expected_output = (
        "Employee Name: Alice\n"
        "Employee Id: E1001\n"
        "Department: IT\n"
        "Salary: 5500\n"
    )
    assert employee_details("Alice","E1001","IT",5500) ==  expected_output