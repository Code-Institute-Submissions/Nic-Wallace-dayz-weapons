# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files. Because of the Django templating language code embedded in the HTML files, the urls can't be directly copied and pasted into the validator. Instead, the source code of each page was pasted into the validator directly.

| Page | Screenshot | Notes |
| --- | --- | --- |
| Home | ![screenshot](documentation/html-validation-home.png) | Pass: No Errors |
| Admin Home | ![screenshot](documentation/html-validation-home.png) | Pass: No Errors |
| Signup | ![screenshot](documentation/html-validation-signup-errors.png) | Error from automatic form formatting, closing tags are present |
| Login | ![screenshot](documentation/html-validation-login.png) | Pass: No Errors |
| Sign Out | ![screenshot](documentation/html-validation-signout.png) | Pass: No Errors |
| Weapon | ![screenshot](documentation/html-validation-weapon.png) | Pass: No Errors |
| Add Weapon | ![screenshot](documentation/html-validation-add-weapon-error.png) | Error: Stray closing div |
| Add Weapon-Fixed | ![screenshot](documentation/html-validation-add-weapon-error-fixed.png) | Pass: No Errors, removed stray closing div |
| Edit Weapon | ![screenshot](documentation/html-validation-edit-weapon.png) | Pass: No Errors |
| Delete Weapon | ![screenshot](documentation/html-validation-delete-weapon.png) | Pass: No Errors |

### CSS

- I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

    ![screenshot](documentation/css-validation-style.png) | Pass: No Errors 

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Nic-Wallace/dayz-weapons/main/inventory/admin.py) | ![screenshot](documentation/py-validation-admin.py.png) | Pass: No Errors |
| forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Nic-Wallace/dayz-weapons/main/inventory/forms.py) | ![screenshot](documentation/py-validation-forms.py.png) | Pass: No Errors |
| models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Nic-Wallace/dayz-weapons/main/inventory/models.py) | ![screenshot](documentation/py-validation-models.py.png) | Pass: No Errors |
| test_forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Nic-Wallace/dayz-weapons/main/inventory/test_forms.py) | ![screenshot](documentation/py-validation-test_forms.py.png) | E302 expected 2 blank lines, found 1. FIXED: No Errors |
| test_views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Nic-Wallace/dayz-weapons/main/inventory/test_views.py) | ![screenshot](documentation/py-validation-test_views.py.png) | Pass: No Errors |
| urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Nic-Wallace/dayz-weapons/main/inventory/urls.py) | ![screenshot](documentation/py-validation-urls.py.png) | Pass: No Errors |
| views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Nic-Wallace/dayz-weapons/main/inventory/views.py) | ![screenshot](documentation/py-validation-views.py.png) | Pass: No Errors |
| settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Nic-Wallace/dayz-weapons/main/main/settings.py) | ![screenshot](documentation/py-validation-settings.py.png) | Pass: No Errors |
| main/urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Nic-Wallace/dayz-weapons/main/main/urls.py) | ![screenshot](documentation/py-validation-main-urls.py.png) | Pass: No Errors |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Signup | Weapon | Notes |
| --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browser-chrome-home.png) | ![screenshot](documentation/browser-chrome-signup.png) | ![screenshot](documentation/browser-chrome-weapon.png) | Works as expected |
| Firefox | ![screenshot](documentation/browser-firefox-home.png) | ![screenshot](documentation/browser-firefox-signup.png) | ![screenshot](documentation/browser-firefox-weapon.png) | Works as expected |
| Opera | ![screenshot](documentation/browser-opera-home.png) | ![screenshot](documentation/browser-opera-signup.png) | ![screenshot](documentation/browser-opera-weapon.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | Signup | Weapon | Notes |
| --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsive-mobile-home.png) | ![screenshot](documentation/responsive-mobile-signup.png) | ![screenshot](documentation/responsive-mobile-weapon.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsive-tablet-home.png) | ![screenshot](documentation/responsive-tablet-signup.png) | ![screenshot](documentation/responsive-tablet-weapon.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsive-desktop-home.png) | ![screenshot](documentation/responsive-desktop-signup.png) | ![screenshot](documentation/responsive-desktop-weapon.png) | Works as expected |
| XL Monitor | ![screenshot](documentation/responsive-xldesktop-home.png) | ![screenshot](documentation/responsive-xldesktop-signup.png) | ![screenshot](documentation/responsive-xldesktop-weapon.png) | Works as expected |
| Xiaomi Redmi Note10 Pro | ![screenshot](documentation/responsive-xiaomi-home.jpg) | ![screenshot](documentation/responsive-xiaomi-signup.jpg) | ![screenshot](documentation/responsive-xiaomi-weapon.jpg) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse-home-desktop.png) | Some minor warnings |
| Signup | ![screenshot](documentation/lighthouse-signup-mobile.png) | ![screenshot](documentation/lighthouse-signup-desktop.png) | Slow response time due to form |
| Weapon | ![screenshot](documentation/lighthouse-weapon-mobile.png) | ![screenshot](documentation/lighthouse-weapon-desktop.png) | Some minor warnings |

## Defensive Programming

I have tested that all user actions cannot break the application.

Pages:
- User can navigate and click on all expected elements
- Prev and Next buttons work
- User will be met with confirmation of actions

Forms:
- They cannot be empty
- On submit, the user is redirected
- email address and password must be valid

Admin:
- Only admin actions will be visible to admin
- Confirmation will be given on actions

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

These tests are found in test_forms.py and test_views.py.

## Bugs

- Form not accepting image uploads

    - To fix this, I set `enctype="multipart/form-data"` onto the form element.

- Python `E501 line too long` (100 > 79 characters)

    - To fix this, I split content onto a new line.

- Python trailing whitespace

    - To fix this, I removed any blank lines that had spaces.

## Unfixed Bugs

To my knowledge, there are no remaining bugs in my code.
