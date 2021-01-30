from service.views import app

#app must be initialized in the same directory than the views

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
