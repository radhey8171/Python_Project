contacts = []
def add_contact():
    name = input("Enter Name:")
    phone = input("Enter Phone:")
    email = input("Enter Email:")
    address = input("Enter Address:" )

    contact = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    contacts.append(contact)
    print("Contact Added Successfully")

def view_contacts():
    if not contacts:
        print("No Contacts Found")
        return
    print("\n-----Contact List-----")
    for i,contact in enumerate(contacts,1):
       print(f"\nContact {i}")
       for key, value in contact.items():
            print(f"{key}: {value}")
def search_contact():
    key = input("Enter Name or Phone: ")
    for contact in contacts:
      if contact["Name"].lower()==key.lower() or contact["Phone"] == key:
        print("\nContact Found")
        for k, v in contact.items():
           print(f"{k}: {v}")
        return
    print("Contact Not Found")
def update_contact():
  name = input("Enter Name to Update: ")
  for contact in contacts:
    if contact["Name"].lower() == name.lower():
       contact["Phone"] = input("New Phone:")
       contact["Email"] = input("New Email:")
       contact["Address"] = input("New Address:")
       print("Contact Updated Successfully!")
       return
    print("Contact Not Found!")
def delete_contact():
   name = input("Enter Name to Delete: ")
   for contact in contacts:
     if contact["Name"].lower()==name.lower():
      contacts.remove(contact)
      print("Contact Deleted Successfully!")
      return
   print("Contact Not Found!")
while True:
   print("\n====== CONTACT BOOK ======")
   print("1.Add Contact")
   print("2.View Contact")
   print("3.Search Contact")
   print("4.Update Contact")
   print("5.Delete Contact")
   print("6.Exit")
   choice = input("Enter Choice:")
   if choice == "1":
      add_contact()
   elif choice == "2":
      view_contacts()
   elif choice == "3":
      search_contact()
   elif choice == "4":
      update_contact()
   elif choice == "5":
      delete_contact()
   elif choice == "6":
      print("Thank You!")
      break
   else:
      print("Invalid Choice!")
                
   




