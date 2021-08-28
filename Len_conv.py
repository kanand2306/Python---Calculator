def length():
    ch=input("\nList of Conversions:\n\n1 : cm to m\n2 : mm to cm\n3 : m to cm\n4 : cm to mm\n5 : mm to m\n6 : m to mm\n7 : km to m\n8 : m to km\n9 : mm to km\n10 : ft to cm\n11 : ft to mm\n12 : ft to inch\n13 : inch to cm\n14 : inch to mm\n\nEnter your choice : ")
    n=input("Enter the number: ")
    if ch=='1':
        print("Output = ",float(n)/100,"m")
    elif ch=='2':
        print("Output = ",float(n)/10,"cm")
    elif ch=='3':
        print("Output = ",float(n)*100,"cm")
    elif ch=='4':
        print("Output = ",float(n)*10,"mm")
    elif ch=='5':
        print("Output = ",float(n)/1000,"m")
    elif ch=='6':
        print("Output = ",float(n)*1000,"mm")
    elif ch=='7':
        print("Output = ",float(n)*1000,"m")
    elif ch=='8':
        print("Output = ",float(n)/1000,"km")
    elif ch=='9':
        print("Output = ",float(n)/1000000,"km")
    elif ch=='10':
        print("Output = ",float(n)*30.48,"cm")
    elif ch=='11':
        print("Output = ",float(n)*304.8,"mm")
    elif ch=='12':
        print("Output = ",float(n)*12,"inch")
    elif ch=='13':
        print("Output = ",float(n)*2.54,"cm")
    elif ch=='14':
        print("Output = ",float(n)*25.4,"mm")
    else:
        print("Wrong Input")



