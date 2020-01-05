# 🅖🅡🅐🅜

## Built By [Dennis](https://github.com/oodennis20/)

## Description
This is aclone of the popular social media application: Instagram. The application allows users to upload, like and comment on other peoples images. Images must have captions and users have profiles where they can see all their images. The admin is  currently responsible for editing or deleting images.
**Users must log in with credible emails**

## User Stories
These are the behaviours/features that the application implements for use by a user.

Users would like to:
* View all images submitted by any user.
* Click on images to display more details.
* Search for users.
* Receive email when signing up.
* Follow others.
* Like Images.


## Admin Abilities
These are the behaviours/features that the application implements for use by the admin.

Admin should:
* Sign in to the application
* Add, Edit and Delete images
* Delete images
* Manage the application.

# [Specifications](Specs.md)

## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv
* Requirements.txt

### Cloning
* In your terminal:

        $ git clone https://github.com/oodennis20/Gram
        $ cd Instrapicha

## Running the Application
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/activate
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Django and other Modules

        $ see Requirements.txt

* To run the application, in your terminal:

        $ python3.6 manage.py runserver

## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py test images

## Technologies Used
* Python3.6
* Django  framework and postgresql database

## Known Bugs
* User must add profile before uploading an image or viewing profiles
* Multiple likes can be done on single image

# [License](License.txt)