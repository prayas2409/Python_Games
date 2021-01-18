def default_printer():
    print("Hi Prayas I can't change name")

def name_printer(name):
    # this method will print what ever name we pass to it
    print("Hi",name)

if __name__ == "__main__":
    #call method without any parameters
    default_printer()
    company_name = "Brigelabz"
    # pass company name to name printer
    name_printer(company_name)
    name_printer("Tata Industries")