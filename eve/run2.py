from eve import Eve

app = Eve()

@app.route('/student/keerthi')
def theStudentKeerthi ():
	return "My name is Keerthi"

if __name__ == '__main__':

	app.run()

