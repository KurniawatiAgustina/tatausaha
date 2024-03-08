from odoo import api, fields, models
from odoo.exceptions import ValidationError

class data_suratmasuk(models.Model):
    _name = 'surat.masuk'
    _description = 'surat masuk'

    no = fields.Integer(string='No')
    tanggal = fields.Date(string='Tanggal')
    nosurat = fields.Integer(string='Nomor')
    tanggalsurat = fields.Date(string='Tanggal')
    tofrom = fields.Char(string='Dari/Kepada')
    ringkasan = fields.Char(string='Ringkasan')
    keterangan = fields.Char(string='Keterangan')
    file_surat = fields.Binary(string='File Surat')
    
class data_suratkeluar(models.Model):
    _name = 'surat.keluar'
    _description = 'surat keluar'

class data_penugasan(models.Model):
    _name = 'data.penugasan'
    _description = 'data_penugasan'
    
    name = fields.Char(string='Nama', required=True)
    jabatan = fields.Char(string='Jabatan', required=True)
    niy = fields.Char(string='NIY', required=True)
    alamat = fields.Char(string='Alamat', required=True)
    jam = fields.Datetime(string='Jam', required=True)
    tempat = fields.Char(string='Tempat', required=True)

    @api.model
    def create(self, vals):
        record = super(data_penugasan, self).create(vals)
        if any(not record[field] for field in ['name', 'jabatan', 'niy', 'alamat', 'jam', 'tempat']):
            self.env['mail.message'].create({
                'body': "Ada kolom yang belum diisi!",
                'model': 'data.penugasan',
                'res_id': record.id,
                'subtype_id': self.env.ref('mail.mt_comment').id,
            })
        else:
            self.env['mail.message'].create({
                'body': "Semua kolom berhasil diisi.",
                'model': 'data.penugasan',
                'res_id': record.id,
                'subtype_id': self.env.ref('mail.mt_comment').id,
            })
        return record