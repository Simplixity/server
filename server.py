"""
Flask dev server module
"""
import simplixity


if __name__ == '__main__':
    print 'Simplixity Server'
    simplixity.app.run(host='0.0.0.0', debug=True)



