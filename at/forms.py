# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms.fields import TextField, RadioField, SelectField, BooleanField, SubmitField, IntegerField, HiddenField
from wtforms.widgets import TextArea
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, NumberRange, optional, ValidationError, Length
import re


def validate_phone_number(form, field):
    pattern = re.compile("^[0-9]+$")
    if not pattern.match(field.data):
        raise ValidationError(u'Số điện thoại không chính xác')

class BaseForm(Form):
    full_name = TextField('full_name', validators=[DataRequired(message=u'Tên không chính xác')])
    email = EmailField('email', validators=[DataRequired(message=u'Email không chính xác'),
                                            Email(message=u'Email không chính xác')])
    phone = TextField('phone', validators=[DataRequired(message=u'Số điện thoại không chính xác'), Length(min=10, max=12), validate_phone_number])
    address = TextField('address', validators=[DataRequired(message=u'Địa chỉ là bắt buộc')])

    aff_sid = TextField('aff_sid', validators=[DataRequired(message=u'')])
    campaign_id = TextField('campaign_id', validators=[DataRequired(message=u'')])
    product_quantity = TextField('product_quantity', validators=[DataRequired(message=u'')])
    product_id = TextField('product_id', validators=[DataRequired(message=u'')])
    product_name = TextField('product_name', validators=[DataRequired(message=u'')])
    product_price = TextField('product_price', validators=[DataRequired(message=u'')])
    submit = SubmitField('Submit')

    def _get_User_Field_Names(self):
        return []

class BaseForm(Form):
    aff_sid = TextField('aff_sid', validators=[DataRequired(message=u'')])
    campaign_id = TextField('campaign_id', validators=[DataRequired(message=u'')])
    product_quantity = TextField('product_quantity', validators=[DataRequired(message=u'')])
    product_id = TextField('product_id', validators=[DataRequired(message=u'')])
    product_name = TextField('product_name', validators=[DataRequired(message=u'')])
    product_price = TextField('product_price', validators=[DataRequired(message=u'')])
    submit = SubmitField('Submit')
    def _get_User_Field_Names(self):
        return ["name", "email", "phone", "address"]

class NutriBabyForm(Form):
    name = TextField('name', validators=[DataRequired(message=u'Tên không chính xác')])
    email = EmailField('email', validators=[DataRequired(message=u'Email không chính xác'),
                                            Email(message=u'Email không chính xác')])
    phone = TextField('Phone',
                      validators=[DataRequired(message=u'Số điện thoại không chính xác'), Length(min=10, max=12),
                                  validate_phone_number])
    address = TextField('address', validators=[DataRequired(message=u'Địa chỉ là bắt buộc')])

    product = SelectField('product', choices=[
        ("Combo_Nutribaby", u"Combo Nutribaby"),
        ("Combo_Nutriplus", u"Combo Nutriplus")
    ], coerce=str)
    product_quantity = IntegerField('product_quantity',
                                    validators=[DataRequired(message=u'Số lượng sản phẩm là bắt buộc')])

    aff_sid = HiddenField("aff_sid")
    campaign_id = HiddenField("campaign_id")
    product_price = HiddenField("product_price")
    submit = SubmitField('Submit')


class Form394(BaseForm):
    # Dat Xanh
    full_name = TextField('full_name', validators=[DataRequired(message=u'Tên không chính xác')])
    phone = TextField('phone',
                      validators=[DataRequired(message=u'Số điện thoại không chính xác'), Length(min=10, max=12),
                                  validate_phone_number])

    def _get_User_Field_Names(self):
        return ["full_name", "phone"]
