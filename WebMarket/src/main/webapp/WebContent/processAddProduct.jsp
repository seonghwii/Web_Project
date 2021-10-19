<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="EUC-KR"%>
    <%@ page import="com.oreilly.servlet.*" %>
    <%@ page import="com.oreilly.servlet.multipart.*" %>
    <%@ page import="java.util.*" %>
    <%@ page import="dto.Product" %>
    <%@ page import="dao.ProductRepository" %>
    
   
<html>
<head>
<title>Insert title here</title>
</head>
<body>
<%
    
    request.setCharacterEncoding("UTF-8");
   
	String filename = "";
	String realFolder = "D:\\MK_Project2\\workspace\\WebMarket\\src\\main\\webapp\\WebContent\\resources\\images";
	//String realFolder = "C:\\upload";
	int maxSize = 5 * 1024 * 1024;
	String encType= "utf-8";
	
	MultipartRequest multi = new MultipartRequest(request, realFolder, maxSize, 
			encType, new DefaultFileRenamePolicy());
	
    String productId = multi.getParameter("productId");
    String name = multi.getParameter("name");
    String unitPrice = multi.getParameter("unitPrice");
    String description = multi.getParameter("description");
    String manufacturer = multi.getParameter("manufacturer");
    String category = multi.getParameter("category");
    String unitsInStock = multi.getParameter("unitsInStock");
    String condition = multi.getParameter("condition");
    System.out.println(productId);
    
    Integer price;
    
    if (unitPrice.isEmpty())
    	price = 0;
    else
    	price = Integer.valueOf(unitPrice);
    
    long stock;
    
    if (unitsInStock.isEmpty()) 
    	stock = 0;
    else
    	stock = Long.valueOf(unitsInStock);
    
    Enumeration files = multi.getFileNames();
    String fname = (String) files.nextElement();
    String fileName = multi.getFilesystemName(fname);
    
    ProductRepository dao = ProductRepository.getInstance();
    
    Product newProduct = new Product();
    newProduct.setProductId(productId);
    newProduct.setPname(name);
    newProduct.setUnitPrice(price);
    newProduct.setDescription(description);
    newProduct.setManufacturer(manufacturer);
    newProduct.setCategory(category);
    newProduct.setUnitsInStock(stock);
    newProduct.setCondition(condition);
    newProduct.setFilename(fileName);
    
    dao.addProduct(newProduct);
    
    response.sendRedirect("products.jsp");
    
    %>
</body>
</html>