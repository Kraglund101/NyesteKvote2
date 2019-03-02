<?php
    $name = $_post['name'];
    $visitor_email = $_post['email'];
    $message = $_post['message'];


    $email_from = '1337kraglund@gmail.com';

    $email_subject = "New Form Submission";

    $email_body = "User name: $name.\n"
                    "User Email: $visitor_email.\n"
                        "User Message: $message.\n";

    $to = "Frederik.kraglund@gmail.com"

    $headers = "From: $email_from \r\n";

    $headers .= "Reply-to: $visitor_email \r\n";

    mail($to,$email_subject,$email_body,$headers);

    header("Location: kontakt.html");