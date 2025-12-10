import qrcode
import image

message = input('what is the message or link you want to contain in your qr code: ')
qrm = qrcode.make(message)
qrd = input('what is the local file destination you want your qr image to be saved')
qrd.replace('\\', '/')
qrn = input('what is the file name u want your file to be saved?: ')
qrm.save(f"{qrd}/{qrn}.jpg")
print('your qr code was saved successfully, please view the file destination you provided')
