# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
import time
from odoo.exceptions import UserError


class travel_management(models.Model):
    _name = 'travel_management.travel_management'
    _description = 'travel_management.travel_management'

    ### Guest Info ###
    name = fields.Char('Travel No')
    
    ### Booking Info ###
    package_id = fields.Many2one('travel_package_master.travel_package_master', 'Package ID')
    package_name = fields.Char('Package Name')
    allowed_guest = fields.Char('Allowed Guest')
    no_of_guest = fields.Integer('No of Guest')
    allowed_days = fields.Char('Allowed Days')
    from_date = fields.Date('From Date')
    to_date = fields.Date('To Date')
    total_amount = fields.Float('Total Amount')
    attachment_ids = fields.Many2many('ir.attachment', 'm2m_travel_management_attachment', 'travel_id',
                                      'attachment_id', string='Attachments', help='Attachments related to this record')
    attachment_char = fields.Char('Attachment2')
    
    state = fields.Selection([('draft', 'Draft'),
        ('confirm', 'WFA'),('approved', 'Approved'),
        ('reject', 'Reject')
            ], string='Status', readonly=True, default='draft')
    reject_remark = fields.Text('Reject Remark')
    rating = fields.Selection([('0', '0'),('1', '1'),
        ('2', '2'), ('3', '3'),
        ('4', '4'), ('5', '5')], string='Rating', default='5')
    
    ## Child Tables Declaration
    line_ids = fields.One2many(
        'ch_guest_details.ch_guest_details',
        'header_id',
        'Child Table', readonly=True)


	
    
    ### Entry Info ###
    company_id = fields.Many2one(
        'res.company',
        'Company Name',
        readonly=True,
        default=lambda self: self.env.user.company_id)
    active = fields.Boolean('Active', default=True)
    user_id = fields.Many2one(
        'res.users',
        'Created By',
        readonly=True,
        default=lambda self: self.env.user.id)
    crt_date = fields.Datetime(
        'Created Date',
        readonly=True,
        default=lambda * a: time.strftime('%Y-%m-%d %H:%M:%S'))
    confirm_date = fields.Datetime('Confirmed Date', readonly=True)
    confirm_user_id = fields.Many2one(
        'res.users', 'Confirmed By', readonly=True)
    approved_date = fields.Datetime('Approved Date', readonly=True)
    approved_user_id = fields.Many2one(
        'res.users', 'Approved By', readonly=True)
    rejected_date = fields.Datetime('Rejected Date', readonly=True)
    rejected_user_id = fields.Many2one(
        'res.users', 'Rejected By', readonly=True)
    update_date = fields.Datetime('Last Updated Date', readonly=True)
    update_user_id = fields.Many2one(
        'res.users', 'Last Updated By', readonly=True)

    @api.onchange('package_id')
    def onchange_package_id(self):
        if self.package_id:
            self.package_name = self.package_id.name
            self.allowed_guest = self.package_id.max_guest
            self.allowed_days = self.package_id.max_days
    
    @api.onchange('no_of_guest','from_date','to_date')
    def onchange_total_amount(self):
        if self.no_of_guest and self.from_date and self.to_date:
            self.total_amount = self.no_of_guest * (int(self.package_id.pkg_amount) * int((self.to_date - self.from_date).days))
    
    def entry_confirm(self):
        """ entry_confirm """
        if self.state == 'draft':
            self.name = self.env['ir.sequence'].next_by_code('travel_management.travel_management', sequence_date=False) or '/'
            self.write({'state': 'confirm',
                        'confirm_user_id': self.env.user.id,
                        'confirm_date': time.strftime('%Y-%m-%d %H:%M:%S')})
        return True
    
    def entry_approve(self):
        """ entry_approve """
        if self.state == 'confirm':
            self.write({'state': 'approved',
                        'approved_user_id': self.env.user.id,
                        'approved_date': time.strftime('%Y-%m-%d %H:%M:%S')})
        return True
    
    def entry_reject(self):
        """ entry_reject """
        if self.state == 'approved':
            if not self.reject_remark:
                raise UserError("EEEEEEEEE")
            self.write({'state': 'reject',
                        'rejected_user_id': self.env.user.id,
                        'rejected_date': time.strftime('%Y-%m-%d %H:%M:%S')})
        return True

    def unlink(self):
        """ Unlink Funtion """
        for rec in self:
            if rec.state in ('approved','reject'):
                raise UserError('Warning, You can not delete this entry')
            if rec.state in ('draft','confirm'):
                models.Model.unlink(rec)
        return True

    def write(self, vals):
        """ write """
        vals.update({'update_date': time.strftime('%Y-%m-%d %H:%M:%S'),
                     'update_user_id': self.env.user.id})
        return super(travel_management, self).write(vals)

class ch_guest_details(models.Model):
    """ Guest Details """
    _name = "ch_guest_details.ch_guest_details"
    _description = "Guest Details"

    header_id = fields.Many2one('travel_management.travel_management', string='Travel Management', index=True, ondelete='cascade')

    name = fields.Char('Guest Name')
    age = fields.Integer('Guest Age')
    sex = fields.Selection([('male','Male'),('female','Female'),('others','Others')], 'Sex')
    mobile_no = fields.Char('Mobile No')
    email = fields.Char('Email', size=256)
    aadhar_no = fields.Char('Aadhar No')
