#!/bin/python3

'''
 ____  ____   ____ 
|  _ \/ ___| / ___|
| |_) \___ \| |    
|  _ < ___) | |___ 
|_| \_\____/ \____|

Remote Shell Call. Call Shells Remotely Over HTTP.
Copyright (C) 2020 Zach Podbielniak

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import subprocess
import sys
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask, request
from flask_restplus import Api, Resource, fields
import oneagent

# Set to False to disable OneAgent
oa_enabled = True
sdk = None
wappinfo = None

app = Flask(__name__)
api = Api(app)


	
@api.route('/health')
class Health(Resource):
	def get(self):
		if oa_enabled:
			wreq = sdk.trace_incoming_web_request(
				wappinfo,
				api.base_url + api.base_path + "health",
				"GET",
				remote_address=request.remote_addr,
				headers=dict(request.headers)
			)
			with wreq:
				wreq.set_status_code(200)

			print("Web Trace")

		return {"status": "healthy"}, 200

command = api.model("Command", {
	"command": fields.String(required=True, description="The shell command to run"),
	"format": fields.String(required=True, description="The output format type: text/plain or application/json")
})


@api.route('/run')
class Run(Resource):
	def get(self):
		if oa_enabled:
			wreq = sdk.trace_incoming_web_request(
				wappinfo,
				api.base_url + api.base_path + "run",
				"GET",
				remote_address=request.remote_addr,
				headers=dict(request.headers)
			)
			with wreq:
				wreq.set_status_code(200)

			print("Web Trace")

		return {"status": "healthy", "message": "Please use a POST"}, 200

	@api.expect(command)
	def post(self):
		if oa_enabled:
			wreq = oneagent.get_sdk().trace_incoming_web_request(
				wappinfo,
				api.base_url + api.base_path + "run",
				"POST",
				remote_address=request.remote_addr,
				headers=dict(request.headers)
			)
	
			output = subprocess.Popen(
				api.payload['command'],
				shell=True,
				stdout=subprocess.PIPE
			).stdout.read()

			with wreq:
				wreq.add_parameter('command', api.payload['command'])
				wreq.add_parameter('format', api.payload['format'])
				wreq.add_parameter('output', output)
				wreq.set_status_code(200)

			print("Web Trace")
		
		# No OneAgent
		else:
			output = subprocess.Popen(
				api.payload['command'],
				shell=True,
				stdout=subprocess.PIPE
			).stdout.read()
		

		if api.payload['format'] == "application/json":
			return {"output": output}, 200
		return output, 200





if __name__ == '__main__':
	if oa_enabled:
		if not oneagent.initialize():
			print("Could not initialize OneAgent SDK")
			sys.exit(1)
		sdk = oneagent.get_sdk()

		wappinfo = sdk.create_web_application_info(
			virtual_host='RSC',
			application_id='RemoteShellCall',
			context_root='/'
		)

	app.run(debug=True)
	if oa_enabled:
		oneagent.shutdown()
