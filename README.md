# Track Client IP Django Project
 Track Client IP Django Project


Objective Of This Is Project Is How to get the user IP address in Django...

In Django, the request headers are obtained from the request object using the META attribute of the request object.
Concepts - by 

1 ) - Syntax. HttpRequest.META.
      Return value. The META attribute returns a dictionary consisting of all available HTTP headers.

2 ) - The HTTP headers X-Forwarded-For (XFF) or REMOTE_ADDR are used to get the original requested IP address.

      The IP address stored in the header will be a comma separated list of IP addresses. For example, ip_addr_1, ip_addr_2, ip_addr_3.
