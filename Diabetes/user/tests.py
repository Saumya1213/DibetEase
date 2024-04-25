from django.test import TestCase

# # Create your tests here.
# <!DOCTYPE html>
# <html lang="en">
# <head>
#   <meta charset="UTF-8">
#   <meta name="viewport" content="width=device-width, initial-scale=1.0">
#   <title>signup</title>
#   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" integrity="sha384-gH2yIJ3lnM0Y+BmJkOtyDepJcqsCteddyJNlnWrH3mBsCqdXqCwYL/WjUIG/X0w/" crossorigin="anonymous">
#   <style>
#     body {
#       background-color: #0dcaf0;
#       color: white;
#       font-family: sans-serif;
#       display: flex; 
#       justify-content: center; 
#       align-items: center; 
#       min-height: 100vh; 
#     }
#     .login-box {
#       background-color: #333333;
#       border-radius: 10px;
#       padding: 30px;
#       width: 400px; 
#     }
#     .login-title {
#       text-align: center;
#       margin-bottom: 20px;
#       font-size: 2rem; 
#     }
#     .form-label {
#       font-size: 1.2rem; 
#     }
#     .form-control {
#       font-size: 1.1rem; 
#       height: 40px; 
#       margin-bottom: 15px; 
#     }
#     .btn-primary {
#       background-color: #0dcaf0;
#       border-color: #0dcaf0;
#       font-size: 1.2rem; 
#       padding: 10px 20px; 
#       margin-top: 20px; 
#     }

#     .email-field {
#         margin-left: 40px; 
#       }
  

#   </style>
# </head>
# <body>
#   <div class="container mt-5">
#     <div class="row d-flex justify-content-center">
#       <div class="col-md-6 login-box">
#         <h2 class="text-center login-title">Not Registered Yet? Create your Account</h2>
#         <div class="card p-4">
          
#           <form action="login/" method="post">
#             {% csrf_token %}
#             <div class="mb-3">
#               <label for="username" class="form-label">Username : </label>
#               <input type="text" class="form-control" id="username" name="username" aria-describedby="usernameHelp" required>
#             </div>
#             <div class="mb-3 email-field">
#               <label for="email" class="form-label">Email    : </label>
#               <input type="email" class="form-control" id="email" name="email" aria-describedby="emailHelp" required>
#             </div>
#             <div class="mb-3">
#               <label for="password" class="form-label">Password : </label>
#               <input type="password" class="form-control" id="password" name="password" required>
#             </div>
#             <div class="d-grid gap-2 mt-3">
#               <button type="submit" class="btn btn-primary">Signup</button>
#             </div>
#           </form>
#         </div>
#       </div>
#     </div>
#   </div>

#   <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-AQRvWUsjQOCZVYEksuONqyQtVV35CWLqQZNgjpzB9iOnYKtx8zWq/LmLjEMBt1JE" crossorigin>





# <!DOCTYPE html>
# <html lang="en">
# <head>
#   <meta charset="UTF-8">
#   <meta name="viewport" content="width=device-width, initial-scale=1.0">
#   <title>login</title>
#   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" integrity="sha384-gH2yIJ3lnM0Y+BmJkOtyDepJcqsCteddyJNlnWrH3mBsCqdXqCwYL/WjUIG/X0w/" crossorigin="anonymous">
#   <style>
#     body {
#       background-color: #0dcaf0;
#       color: white;
#       font-family: sans-serif;
#       display: flex; /* Added for vertical centering */
#       justify-content: center; /* Added for vertical centering */
#       align-items: center; /* Added for vertical centering */
#       min-height: 100vh; /* Added for vertical centering (full viewport height) */
#     }
#     .login-box {
#       background-color: #333333;
#       border-radius: 10px;
#       padding: 30px;
#       width: 400px; /* Maintained width */
#     }
#     .login-title {
#       text-align: center;
#       margin-bottom: 20px;
#       font-size: 2rem; /* Increased font size */
#     }
#     .form-label {
#       font-size: 1.2rem; /* Increased label font size */
#     }
#     .form-control {
#       font-size: 1.1rem; /* Increased input field font size */
#       height: 40px; /* Increased input field height */
#       margin-bottom: 15px; /* Added spacing between fields */
#     }
#     .btn-primary {
#       background-color: #0dcaf0;
#       border-color: #0dcaf0;
#       font-size: 1.2rem; /* Increased button font size */
#       padding: 10px 20px; /* Increased button padding */
#       margin-top: 20px; /* Added spacing above button */
#     }

  

#   </style>
# </head>
# <body>
#   <div class="container mt-5">
#     <div class="row d-flex justify-content-center">
#       <div class="col-md-6 login-box">
#         <h2 class="text-center login-title">Already Registered? Login </h2>
#         <div class="card p-4">
          
#           <form action="dashboard/" method="post"> 
#             {% csrf_token %}
#             <div class="mb-3">
#               <label for="username" class="form-label">Username : </label>
#               <input type="text" class="form-control" id="username" name="username" aria-describedby="usernameHelp" required>
#             </div>
            
#             <div class="mb-3">
#               <label for="password" class="form-label">Password : </label>
#               <input type="password" class="form-control" id="password" name="password" required>
#             </div>
#             <div class="d-grid gap-2 mt-3">
#               <button type="submit" class="btn btn-primary">Login</button>
#             </div>
#           </form>
#         </div>
#       </div>
#     </div>
#   </div>

#   <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-AQRvWUsjQOCZVYEksuONqyQtVV35CWLqQZNgjpzB9iOnYKtx8zWq/LmLjEMBt1JE" crossorigin>
