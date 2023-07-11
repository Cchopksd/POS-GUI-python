def fetch_Tree(pageNAME,mytree,cursor) :
    if pageNAME == "HOME" :
        mytree.delete(*mytree.get_children())
        sql = "SELECT * FROM product"
        cursor.execute(sql)
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result):
                mytree.insert('', 'end', values=(data[1],data[0],data[2]))
    elif pageNAME == "MANAGE_EMPLOYEE" :
        mytree.delete(*mytree.get_children())
        sql = "SELECT * FROM employee WHERE employee_permission = ?"
        cursor.execute(sql,["พนักงาน"])
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result):
                mytree.insert('', 'end', values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9]))
    elif pageNAME == "REGISTER_EMPLOYEE" :
        mytree.delete(*mytree.get_children())
        sql = "SELECT * FROM employee WHERE employee_permission = ?"
        cursor.execute(sql,["พนักงาน"])
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result):
                mytree.insert('', 'end', values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9]))
    elif pageNAME == "EDIT_EMPLOYEE" :
        mytree.delete(*mytree.get_children())
        sql = "SELECT * FROM employee WHERE employee_permission = ?"
        cursor.execute(sql,["พนักงาน"])
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result):
                mytree.insert('', 'end', values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9]))
    elif pageNAME == "HISTORY_EMPLOYEE" :
        mytree.delete(*mytree.get_children())
        sql = "SELECT * FROM orderlist"
        cursor.execute(sql)
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result):
                mytree.insert('', 'end', values=(data[0],data[1],data[2],data[3],data[4]))
    elif pageNAME == "MANAGE_CUSTOMER" :
        mytree.delete(*mytree.get_children())
        sql = "SELECT * FROM member"
        cursor.execute(sql)
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result):
                mytree.insert('', 'end', values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))
    elif pageNAME == "MANAGE_PRODUCT" :
        mytree.delete(*mytree.get_children())
        sql = "SELECT * FROM product"
        cursor.execute(sql)
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result):
                mytree.insert('', 'end', values=(data[1],data[0],data[2]))
    elif pageNAME == "MANAGE_STOCK" :
        mytree.delete(*mytree.get_children())
        sql = "SELECT * FROM staple"
        cursor.execute(sql)
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result):
                mytree.insert('', 'end', values=(data[0],data[1],data[2]))
    
    elif pageNAME == "ORDER_STOCK" :
        # print("asd")
        mytree.delete(*mytree.get_children())
        sql = "SELECT * FROM staple"
        cursor.execute(sql)
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result):
                mytree.insert('', 'end', values=(data[0],data[1],data[2]))

    elif pageNAME == "REQUISITION" :
        mytree.delete(*mytree.get_children())
        sql = "SELECT * FROM staple"
        cursor.execute(sql)
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result):
                mytree.insert('', 'end', values=(data[0],data[1],data[2]))