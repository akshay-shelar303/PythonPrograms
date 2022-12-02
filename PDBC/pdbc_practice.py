'''
import MySQLdb
conn=MySQLdb.connect('localhost','root','root','akshay')
curs=conn.cursor()

print(" Select your choice---\n1.CREATE TABLE\n2.INSERT DATA\n3.UPDATE DATA\n4.DELETE DATA\n5.DATA RETRIVE")
ch=int(input('Enter your choice-'))

if ch==1:
    tbl_name=input('enter table name-')
    cre=f"create table {tbl_name}(id int,name varchar(30),amount varchar(30));"
    curs.execute(cre)

elif ch==2:
    id=int(input('Enter customer id-'))
    name=input('Enter customer name-')
    amount=int(input('Enter customer amount-'))
    ins=f"insert into customer values({id},'{name}',{amount});"
    curs.execute(ins)

elif ch==3:
    up="update customer set amount=2200 where id =3"
    curs.execute(up)

elif ch==4:
    dlt="delete from customer where  id=3"
    curs.execute(dlt)

elif ch==5:
    
    data="select * from customer;"
    curs.execute(data)
    for rows in curs:
        print(rows)

conn.commit()
conn.close()
'''
'''
import MySQLdb
conn=MySQLdb.connect('localhost','root','root','akshay')
curs=conn.cursor()

print(" Select your choice---\n1.CREATE TABLE\n2.INSERT DATA\
\n3.UPDATE DATA\n4.DELETE DATA\n5.DATA RETRIVE")
ch=int(input('Enter your choice-'))

if ch==1:
    tbl_name=input('Enter table name-')
    col1=input('Enter column 1 and datatype-')
    col2=input('enter column 2 and datatype-')
    col3=input('enter column3 and datatype-')

    cre=f"create table {tbl_name}({col1},{col2},{col3});"
    curs.execute(cre)

elif ch==2:
    tbl_name=input('Enter table name-')
    val1=int(input('Enter column1 value -'))
    val2=input('enter column2 value-')
    val3=int(input('enter column2 value -'))
    ins=f"insert into {tbl_name} values({val1},'{val2}',{val3});"
    curs.execute(ins)
    

elif ch==3:
    tbl_name=input('Enter table name-')
    col_name=input('Enter colunm name-')
    value=input('Enter values tobe update-')
    condition=input("Enter condition-")
    upd=f"update {tbl_name} set {col_name}='{value}' where {condition};"
    curs.execute(upd)

elif ch==4:
    tbl_name=input('Enter table name-')
    condition=input("Enter condition-")
    dlt=f"delete from {tbl_name} where {condition};"
    curs.execute(dlt)

elif ch==5:
    tbl_name=input('Enter table name-')
    data=f"select * from {tbl_name};"
    curs.execute(data)
    for rows in curs:
        print(rows)
            
conn.commit()
conn.close()


'''



'''
import MySQLdb
conn=MySQLdb.connect('localhost','root','root','akshay')
curs=conn.cursor()

print(" Select your choice---\n1.CREATE TABLE\n2.INSERT DATA\
\n3.UPDATE DATA\n4.DELETE DATA\n5.DATA RETRIVE")
ch=int(input('Enter your choice-'))

if ch==1:
    tbl_name=input('Enter table name-')
    col1=input('Enter column 1 and datatype-')
    col2=input('enter column 2 and datatype-')
    col3=input('enter column3 and datatype-')

    cre=f"create table {tbl_name}({col1},{col2},{col3});"
    curs.execute(cre)

elif ch==2:
    tbl_name=input('Enter table name-')
    val1=int(input('Enter column1 value -'))
    val2=input('enter column2 value-')
    val3=int(input('enter column2 value -'))
    ins=f"insert into {tbl_name} values({val1},'{val2}',{val3});"
    curs.execute(ins)
    
elif ch==3:
    tbl_name=input('Enter table name-')
    col_name=input('Enter colunm name-')
    value=input('Enter values tobe update-')
    condition=input("Enter condition-")
    upd=f"update {tbl_name} set {col_name}='{value}' where {condition};"
    curs.execute(upd)

elif ch==4:
    tbl_name=input('Enter table name-')
    condition=input("Enter condition-")
    dlt=f"delete from {tbl_name} where {condition};"
    curs.execute(dlt)

elif ch==5:
    tbl_name=input('Enter table name-')
    data=f"select * from {tbl_name};"
    curs.execute(data)
    for rows in curs:
        print(rows)

elif ch==6:
    tbl_name=input('Enter table name-')
    col_name=input('Enter colunm name-')
    pk=f"alter table {tbl_name} add constraint pk1 primary key({col_name});"
    curs.execute(pk)

elif ch==7:
    pri_tbl_name=input('Enter  primary key table name-')
    tbl_name=input('Enter table name on which foreign key is applied-')
    pri_col_name=input('Enter primary column name-')
    col_name=input('Enter colunm name on which foreign key is applied-')
    fk=f"alter table {tbl_name} add constraint fk1 foreign key({col_name}) references {pri_tbl_name}({pri_col_name});"
    curs.execute(fk)

elif ch==8:
    tbl_name=input('Enter table name-')
    s=f"show create table {tbl_name};"
    curs.execute(s)
    for i in curs:
        print(i)

else:
    print('Invalid input ')
    
conn.commit()
conn.close()

'''
'''
import MySQLdb
conn=MySQLdb.connect('localhost','root','root','new')
curs=conn.cursor()

print(" Select your choice---\n1.CREATE TABLE\n2.INSERT DATA\
\n3.UPDATE DATA\n4.DELETE DATA\n5.DATA RETRIVE\
\n6.Add primary key\n7.Add Foreign key")
ch=int(input('Enter your choice-'))

if ch==1:
    tbl_name=input('Enter table name-')
    col1=input('Enter column 1 and datatype-')
    col2=input('enter column 2 and datatype-')
    col3=input('enter column3 and datatype-')

    cre=f"create table {tbl_name}({col1},{col2},{col3});"
    curs.execute(cre)


elif ch==2:
    tbl_name=input('Enter table name-')
    val1=int(input('Enter column1 value -'))
    val2=input('enter column2 value-')
    val3=int(input('enter column3 value -'))
    ins=f"insert into {tbl_name} values({val1},'{val2}',{val3});"
    curs.execute(ins)
    
elif ch==3:
    tbl_name=input('Enter table name-')
    col_name=input('Enter colunm name-')
    
    if type(col_name)==str:
        value=input('Enter values tobe update-')
        condition=input("Enter condition-")
        upd=f"update {tbl_name} set {col_name}='{value}' where {condition};"
        curs.execute(upd)
    elif type(col_name)==int:
        value=input('Enter values tobe update-')
        condition=input("Enter condition-")
        upd=f"update {tbl_name} set {col_name}={value} where {condition};"
        curs.execute(upd)
        

elif ch==4:
    tbl_name=input('Enter table name-')
    condition=input("Enter condition-")
    dlt=f"delete from {tbl_name} where {condition};"
    curs.execute(dlt)

elif ch==5:
    tbl_name=input('Enter table name-')
    data=f"select * from {tbl_name};"
    curs.execute(data)
    for rows in curs:
        print(rows)

elif ch==6:
    tbl_name=input('Enter table name-')
    col_name=input('Enter colunm name-')
    pk=f"alter table {tbl_name} add constraint pk1 primary key({col_name});"
    curs.execute(pk)

elif ch==7:
    pri_tbl_name=input('Enter  primary key table name-')
    tbl_name=input('Enter table name on which foreign key is applied-')
    pri_col_name=input('Enter primary column name-')
    col_name=input('Enter colunm name on which foreign key is applied-')
    cons_id=input('Enter constraint id-')
    fk=f"alter table {tbl_name} add constraint {cons_id} foreign key({col_name}) references {pri_tbl_name}({pri_col_name}) \
on delete cascade on update cascade;"
    curs.execute(fk)

elif ch==8:
    pri_tbl_name=input('Enter  primary key table name-')
    tbl_name=input('Enter table name on which foreign key is applied-')
    pri_col_name=input('Enter primary column name-')
    col_name=input('Enter colunm name on which foreign key is applied-')
    cons_id=input('Enter constraint id-')
    fk=f"alter table {tbl_name} add constraint {cons_id} foreign key({col_name}) references {pri_tbl_name}({pri_col_name}) \
on delete set null on update set null;"
    curs.execute(fk)

elif ch==9:
    tbl_name=input('Enter table name-')
    col_name=input('Enter column name-')
    add=f"alter table {tbl_name} add column {col_name};"
    curs.execute(add)

elif ch==10:
    join_type=input('Enter type of join-')
    tbl1_name=input('Enter table 1 name-')
    tbl2_name=input('Enter table 2 name-')
    matching_columns=input('Enter matching columns from both tables-')

    jn=f"select * from {tbl1_name} {join_type} {tbl2_name} on {matching_columns};"
    curs.execute(jn)


elif ch==11:
    tbl_name=input('Enter table name-')
    s=f"show create table {tbl_name};"
    curs.execute(s)
    for i in curs:
        print(i)

else:
    print('Invalid input ')
    
conn.commit()
conn.close()
'''



import MySQLdb
conn=MySQLdb.connect('localhost','root','root','new')
curs=conn.cursor()

try:
    print(" Select your choice---\n1.CREATE TABLE\n2.INSERT DATA\
    \n3.UPDATE DATA\n4.DELETE DATA\n5.DATA RETRIVE\
    \n6.Add primary key\n7.Add Foreign key")
    ch=int(input('Enter your choice-'))

    if ch==1:
        tbl_name=input('Enter table name-')
        col1=input('Enter column 1 and datatype-')
        col2=input('enter column 2 and datatype-')
        col3=input('enter column3 and datatype-')

        cre=f"create table {tbl_name}({col1},{col2},{col3});"
        curs.execute(cre)


    elif ch==2:
        tbl_name=input('Enter table name-')
        val1=int(input('Enter column1 value -'))
        val2=input('enter column2 value-')
        val3=int(input('enter column3 value -'))
        ins=f"insert into {tbl_name} values({val1},'{val2}',{val3});"
        curs.execute(ins)
        
    elif ch==3:
        tbl_name=input('Enter table name-')
        col_name=input('Enter colunm name-')
        
        if type(col_name)==str:
            value=input('Enter values tobe update-')
            condition=input("Enter condition-")
            upd=f"update {tbl_name} set {col_name}='{value}' where {condition};"
            curs.execute(upd)
        elif type(col_name)==int:
            value=input('Enter values tobe update-')
            condition=input("Enter condition-")
            upd=f"update {tbl_name} set {col_name}={value} where {condition};"
            curs.execute(upd)
            

    elif ch==4:
        tbl_name=input('Enter table name-')
        condition=input("Enter condition-")
        dlt=f"delete from {tbl_name} where {condition};"
        curs.execute(dlt)

    elif ch==5:
        tbl_name=input('Enter table name-')
        data=f"select * from {tbl_name};"
        x=curs.execute(data)
        if x==0:
            print('No record found in table')
        else:
            for rows in curs:
                print(rows)

    elif ch==6:
        tbl_name=input('Enter table name-')
        col_name=input('Enter colunm name-')
        pk=f"alter table {tbl_name} add constraint pk1 primary key({col_name});"
        curs.execute(pk)


    elif ch==7:
        pri_tbl_name=input('Enter  primary key table name-')
        tbl_name=input('Enter table name on which foreign key is applied-')
        pri_col_name=input('Enter primary column name-')
        col_name=input('Enter colunm name on which foreign key is applied-')
        cons_id=input('Enter constraint id-')
        fk=f"alter table {tbl_name} add constraint {cons_id} foreign key({col_name}) references {pri_tbl_name}({pri_col_name}) \
    on delete cascade on update cascade;"
        curs.execute(fk)
        
except ValueError as e:
    print('you have entered invalid input type',e)
    
except NameError as e:
    print('Name does not exist',e)
    
except MySQLdb._exceptions.OperationalError as e:
    print(e)
    
except MySQLdb._exceptions.ProgrammingError as e:
    print(e)
    
except MySQLdb._exceptions.IntegrityError as e:
    print(e)

else:
    print('No exception ocuur')
    
finally:
    conn.commit()
    conn.close()




















