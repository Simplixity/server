"""
Flask dev server module
"""
import simplixity


if __name__ == '__main__':
    print 'Simplixity Server'
    simplixity.app.run(debug=True)


