# Manual and Automated Testing

Both manual and automated testing were crucial in ensuring my website was functional. Manual testing verified key features including booking, editing, and canceling courts, from both user and admin perspectives, ensuring usability and workflow correctness. By simulating real user interactions such as creating an account, making court bookings, it helps identify bugs, improve user experience, and ensure the site meets functional requirements.

I also performed some automated testing on the forms, models, views and urls. This helped to verify that each component of the tennis booking website functions as expected. They quickly ensure data integrity, validate routing, and confirm form behavior. The use of automated testing increases reliability and reduces the risk of introducing bugs during updates or new feature additions.

# Table of Contents

- [Code Validation](#code-validation)
- [Lighthouse](#lighthouse-testing)
- [Responsiveness](#responsiveness-testing)
- [Browser Compatibility](#browser-compatibility-testing)
- [Automated Testing of user stories](#automated-testing-of-user-stories)

## Code Validation

### HTML

- HTML code was tested using the [W3C Validator](https://validator.w3.org/) via url.

- I received 8 info alerts from the HTML validator relating to trailing slashes. This is due to the add on prettier formatting my HTML and they cannot be removed. The trailing slash on void elements doesn’t affect rendering or cause any errors in my code.

- Initially, the `home.html` and `register.html` templates triggered a semantic HTML warning because they each contained a `<h1>` element, while `base.html` already included a `<h1>`. To resolve this, the page-specific headings were changed to `<h2>` to maintain proper heading hierarchy and improve accessibility.

<details>
<summary>Screenshots and results for all templates.</summary>
<br>

**HOME**

![No Errors or Warnings to show](booking/static/booking/images/validation/html_validator_home.png)

**LOG IN**

![No Errors or Warnings to show](booking/static/booking/images/validation/html_validator_login.png)

**REGISTER**

![No Errors or Warnings to show](booking/static/booking/images/validation/html_validator_register.png)

**My Bookings**

![No Errors or Warnings to show](booking/static/booking/images/validation/html_validator_my_bookings.png)

**Edit Booking**

![No Errors or Warnings to show](booking/static/booking/images/validation/html_validator_book_edit.png)

</details>

<br>

### CSS

- CSS code was tested using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) via text input.

- Some validator warnings appeared for lines using CSS variables (e.g., var(--main-color)). These are informational only because the validator cannot determine dynamic values. They do not indicate errors, and the CSS works correctly in browsers.

<p align="center">
  <img src="booking/static/booking/images/validation/css_validator_warnings.png" alt="CSS validator warnings">
</p>
<details>

<summary>Screenshot with results for the styles.css file</summary>

**styles.css**

![No Error Found](booking/static/booking/images/validation/css_validator_clear.png)

</details>

<br>

### Python

Python code was tested using [Code Institute's Python Linter](https://pep8ci.herokuapp.com/).

<details>

<summary>Screenshots and results for all python files</summary>

- settings.py

Line too long warning for line 85, 87, 88, 112 was unaltered as it is Django code and not making any alterations as advised by fellow Discord members.

![All clear, no errors found](booking/static/booking/images/validation/linter_settings.png)

- tennis urls.py

![All clear, no errors found](booking/static/booking/images/validation/linter_tennis_urls.png)

- booking urls.py

![All clear, no errors found](booking/static/booking/images/validation/linter_booking_urls.png)

- admin.py

![All clear, no errors found](booking/static/booking/images/validation/linter_admin.png)

- apps.py

![All clear, no errors found](booking/static/booking/images/validation/linter_apps.png)

- forms.py

![All clear, no errors found](booking/static/booking/images/validation/linter_forms.png)

- models.py

![All clear, no errors found](booking/static/booking/images/validation/linter_forms.png)

- views.py

![All clear, no errors found](booking/static/booking/images/validation/linter_views.png)

- Testing test_urls.py

![All clear, no errors found](booking/static/booking/images/validation/test_urls_validator.png)

- Testing test_forms.py

![All clear, no errors found](booking/static/booking/images/validation/test_forms_validator.png)

- Testing test_models.py

![All clear, no errors found](booking/static/booking/images/validation/test__models_validator.png)

- Testing test_views.py

![All clear, no errors found](booking/static/booking/images/validation/test_views_validator.png)

</details>

<br>

### JavaScript

The JavaScript code was tested using [JS Hint](https://jshint.com/).

<details>

<summary>Screenshots and results for JavaScript files</summary>

- booking.js

![All clear, no errors found](booking/static/booking/images/validation/jshint_booking_validator.png)

</details>

<br>

## Lighthouse Testing

[Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used to audit the website for performance, accessibility, best practice and SEO. This was run in Chrome DevTools in incognito mode.

- At the beginning of the Lighthouse testing, I noticed the performace of my website being negated by the high quality of my homepage image.
  The performance rating was greatly improved upon the reduction of the file size.

<p align="center">
  <img src="booking/static/booking/images/validation/lighthouse_mobile_home_bad_perf.png" alt="CSS validator warnings">
</p>

- I also had to edit my HTML so that it followed HTML semantics as this was negatively affecting the accessibility score.

<details>
<summary>Screenshots and results for all pages</summary>

**HOME**

- Mobile

![Passed](booking/static/booking/images/validation/lighthouse_mobile_home.png)

- Desktop

![Passed](booking/static/booking/images/validation/lighthouse_home_desktop.png)

**Login**

- Mobile

![Passed](booking/static/booking/images/validation/lighthouse_mobile_signin.png)

- Desktop

![Passed](booking/static/booking/images/validation/lighthouse_desktop_signin.png)

**Register**

- Mobile

![Passed](booking/static/booking/images/validation/lighthouse_mobile_register.png)

- Desktop

![Passed](booking/static/booking/images/validation/lighthouse_desktop_register.png)

**Book**

- Mobile

![Passed](booking/static/booking/images/validation/lighthouse_mobile_book.png)

- Desktop

![Passed](booking/static/booking/images/validation/lighthouse_desktop_book.png)

**My Bookings**

- Mobile

![Passed](booking/static/booking/images/validation/lighthouse_mobile_my_bookings.png)

- Desktop

![Passed](booking/static/booking/images/validation/lighthouse_desktop_my_bookings.png)

**Edit Booking**

- Mobile

![Passed](booking/static/booking/images/validation/lighthouse_mobile_edit_bookings.png)

- Desktop

![Passed](booking/static/booking/images/validation/lighthouse_desktop_edit_bookings.png)

</details>

<br>

## Responsiveness Testing

The website is responsive for screens with a mininum width of 320px and a maximum width of 2560px. Friends tested the website on their devices and found the website responsive. Further manual tests were done using [Chrome's DevTools](https://developer.chrome.com/docs/devtools) and the website proved to be responsive.

<details>

<summary>Screenshots of website at different screen sizes.</summary>

**Responsiveness on different devices**

        Mobile - Asus Zenfone 8

![ Asus Zenfone 8](booking/static/booking/images/responsiveness/responsiveness1.jpg)

        Mobile - Asus Zenfone 8

![Asus Zenfone 8](booking/static/booking/images/responsiveness/responsiveness_about.jpg)

        Tablet - iPad 6 - horizontal

![ipad 6](booking/static/booking/images/responsiveness/ipad_horizontal.jpg)

        Tablet - iPad 6 - vertical

![ipad 6](booking/static/booking/images/responsiveness/ipad_vertical.jpg)

<br>

</details>

<br>

## Browser Compatibility Testing

Website was tested on current Chrome, Firefox and Edge for compatibility.

<details>

<summary>Table of the results.</summary>

| Intended       | Chrome | Firefox | Edge | Safari |
| -------------- | ------ | ------- | ---- | ------ |
| Appearance     | Good   | Good    | Good | Good   |
| Responsiveness | Good   | Good    | Good | Good   |

**Responsiveness on different devices**

        Chrome Browser

![Home on mobile](booking/static/booking/images/responsiveness/responsiveness1.jpg)

        Firefox Browser

![Home on Desktop](booking/static/booking/images/responsiveness/firefox_view.png)

        Edge Browser

![Register on desktop](booking/static/booking/images/responsiveness/edge_register.png)

</details>

<br>

## Automated Testing of User Stories

- The use of automated testing ensures the app works correctly and that all user stories developed using agile methodology have been achieved as expected. It enables catching bugs early and verifying forms, models, URLs, and views behave as expected. It allows safe updates and feature additions. This improves reliability, maintainability, and overall confidence in the project’s functionality.

- The booking/tests/test_forms.py file ensures that the BookingForm correctly validates user input, including required fields and logical constraints like start and end times.

- The booking/tests/test_models.py verifies the Booking model’s behavior, checking that bookings conform to rules such as hourly start times and can be saved properly.
- The booking/tests/test_urls.py confirms that URL patterns resolve to the correct views, ensuring proper routing.

- Finally, the booking/tests/test_views.py tests the views’ functionality, including access control, form submission, and page responses, ensuring the web interface behaves as expected for both authenticated and anonymous users.

![Passed](booking/static/booking/images/validation/testing_py.png)
