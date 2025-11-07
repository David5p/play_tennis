# Manual and Automated Testing

Both manual and automated testing were crucial in ensuring my website was functional. Manual testing ensured all features worked as intended. This included testing booking, editing, and canceling court bookings. This was tested from the user login and admin side. It verifies usability, detects interface issues, and confirms workflow logic. By simulating real user interactions such as creating an account, making court bookings, it helps identify bugs, improve user experience, and ensure the site meets functional requirements.

I also performed some automated testing on the forms, models, views and urls. This helped to verify that each component of the tennis booking website functions as expected. They quickly ensure data integrity, validate routing, and confirm form behavior. The use of automated testing increases reliability and reduces the risk of introducing bugs during updates or new feature additions.

# Table of Contents

- [Code Validation](#code-validation)
- [Lighthouse](#lighthouse-testing)
- [Responsiveness](#responsiveness-testing)
- [Browser Compatibility](#browser-compatibilty-testing)
- [User Stories](#user-story-testing)

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
