import urllib.parse
from sqlmodel import Field, Session, SQLModel, create_engine,select,func,funcfilter,within_group
from typing import Optional
from pydantic import condecimal
from datetime import date, datetime
from decimal import Decimal




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
    voucher_date: Optional[date]
    voucher_no: str = Field(max_length=100, index=True)
    company: str = Field(max_length=150)
    book: str = Field(max_length=150)
    supplier: str = Field(max_length=250)
    vat_reg: str = Field(max_length=100)
    tin_no: str = Field(max_length=70)
    net_of_vat: Decimal = Field(default=0, max_digits=20, decimal_places=2)
    vat_exempt: Decimal = Field(default=0, max_digits=20, decimal_places=2)
    net_ofvat_with_vat_exempt: Decimal = Field(default=0, max_digits=20, decimal_places=2)
    amount_due: Decimal = Field(default=0, max_digits=20, decimal_places=2)
    with_holding_tax: Decimal = Field(default=0, max_digits=20, decimal_places=2)
    total_amount_due: Decimal = Field(default=0, max_digits=20, decimal_places=2)
    expense_account: str = Field(max_length=200)
    description: str = Field(max_length=4000)
    inclusive_date: str = Field(default=None)
    sin: str =Field(default=None)
    can: str =Field(default=None)
    khw_no: Decimal = Field(default=0, max_digits=9, decimal_places=2)
    price: Decimal = Field(default=0, max_digits=9, decimal_places=2)
    cubic_meter: Decimal = Field(default=0, max_digits=9, decimal_places=2)
    pic: str = Field(default=None)
    person_incharge_end_user: str = Field(default=None)
    no_of_person: Decimal = Field(default=0, max_digits=9, decimal_places=2)
    activity_made: str = Field(default=None)
    plate_no: str = Field(default=None)
    user: str =Field(default=None)
    date_updated: Optional[datetime] = Field(default=None)
    date_credited: datetime = Field(default_factory=datetime.utcnow)

class CostHandling():# this is for views function for GRC project

    @staticmethod
    def insert_cost_from_purchase_monitoring(voucher_date,voucher_no,company,
                                             book,supplier,vat_reg,tin_no,net_of_vat,vat_exempt,net_ofvat_with_vat_exempt,
                                             amount_due,with_holding_tax,total_amount_due,expense_account,description,
                                             inclusive_date,sin,can,khw_no,
                                             price,cubic_meter,pic,person_incharge_end_user,
                                             no_of_person,activity_made,plate_no,user):
       
        insertData = Cost(voucher_date=voucher_date,voucher_no=voucher_no,company=company,
                          book=book,supplier=supplier,vat_reg=vat_reg,tin_no=tin_no,
                          net_of_vat=net_of_vat,vat_exempt=vat_exempt,net_ofvat_with_vat_exempt=net_ofvat_with_vat_exempt,amount_due=amount_due,
                          with_holding_tax=with_holding_tax,total_amount_due=total_amount_due,expense_account=expense_account,
                          description=description,inclusive_date=inclusive_date,sin=sin,
                           can=can,khw_no=khw_no,price=price,cubic_meter=cubic_meter,
                             pic=pic,person_incharge_end_user=person_incharge_end_user,
                             no_of_person=no_of_person,activity_made=activity_made,plate_no=plate_no,user=user)

        session = Session(engine)

        session.add(insertData)
        
        session.commit()

        session.close()
