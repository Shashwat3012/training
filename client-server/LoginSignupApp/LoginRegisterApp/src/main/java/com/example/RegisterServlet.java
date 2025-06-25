package com.example;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.IOException;
import java.util.HashMap;

public class RegisterServlet extends HttpServlet {
    public static HashMap<String, String> users = new HashMap<>();

    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        String user = request.getParameter("username");
        String pass = request.getParameter("password");

        if (!users.containsKey(user)) {
            users.put(user, pass);
        }
        response.sendRedirect("login.jsp?error=Registration+successful,+please+login.");
    }
}
