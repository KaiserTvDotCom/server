from flask import Flask, send_file, request

app = Flask(__name__)

@app.route('/firmware_update')
def firmware_update():
    current_version = request.args.get('version')
    latest_version = '1.1'  # última versión del firmware
    if current_version != latest_version:
        print('32 sin actualizar')
        firmware_file = 'firmware.bin'
        return send_file(firmware_file, as_attachment=False)
    else:
        return '', 304  # Notificar al ESP32 que no hay actualizaciones disponibles

if __name__ == '__main__':
    app.run(host='192.168.0.148', port=80)
   



