import qrcode

upi_id = input("Enter your UPI ID: ")

#upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE

#URL making 
Gpay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name'
Paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name'
Phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name'

#QR Code generate
Gpay_qr = qrcode.make(Gpay_url)
Paytm_qr = qrcode.make(Paytm_url)
Phonepe_qr = qrcode.make(Phonepe_url)

#image save
Gpay_qr.save("Gpay_url.png")
Paytm_qr.save("Paytm_url.png")
Phonepe_qr.save("Phonepe_url.png")

#Show
Gpay_qr.show()
Paytm_qr.show()
Phonepe_qr.show()
