import urllib.parse
from sqlmodel import Field, Session, SQLModel, create_engine,select,func,funcfilter,within_group
from typing import Optional
from pydantic import condecimal
from datetime import date, datetime




connection_string = "mysql+pymysql://{user}:{password}@{host}:{port}/{database}".format(
    user="joeysabusido",
    password=urllib.parse.quote("Genesis@11"),
    host="192.46.225.247",
    port=3306,
    database="duravilleDB"
)


engine = create_engine(connection_string, echo=True)

    

class Cost(SQLModel, table=True):
    """This is for table of cost"""
    __tablename__ = 'cost'
    id: Optional[int] = Field(default=None, primary_key=True)
    voucher_date: datetime
    voucher_no: str = Field(max_length=100)
    company: str = Field(max_length=150)
    book: str = Field(max_length=150)
    supplier: str = Field(max_length=250)
    vat_reg: str = Field(max_length=100)
    tin_no: str = Field(max_length=70)
    net_of_vat: condecimal(max_digits=20, decimal_places=2) = Field(default=0)
    amount_due: condecimal(max_digits=20, decimal_places=2) = Field(default=0)
    expense_account: str
    description: str
    user: str =Field(default=None)
    date_updated: Optional[datetime] = Field(default=None)
    date_credited: datetime = Field(default_factory=datetime.utcnow)

class CostHandling():# this is for views function for GRC project

    @staticmethod
    def insert_cost_from_purchase_monitoring(voucher_date,voucher_no,company,
                                             book,supplier,vat_reg,tin_no,net_of_vat,
                                             amount_due,expense_account,description,user):
       
        insertData = Cost(voucher_date=voucher_date,voucher_no=voucher_no,company=company,
                          book=book,supplier=supplier,vat_reg=vat_reg,tin_no=tin_no,
                          net_of_vat=net_of_vat,amount_due=amount_due,expense_account=expense_account,
                          description=description,user=user)

        session = Session(engine)

        session.add(insertData)
        
        session.commit()

        session.close()
