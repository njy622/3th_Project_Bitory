package com.example.demo.Controller;


import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.util.List;
import java.util.Map;
import org.springframework.http.*;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.HttpServerErrorException;
import org.springframework.web.client.RestTemplate;


@Controller
public class PythonController {

    private final String FASTAPI_SERVER_URL = "http://127.0.0.1:8000";

    private final RestTemplate restTemplate = new RestTemplate();

    // 마켓리스트 
    @GetMapping("/pythonapi")
    public String callFastAPI(Model model) {
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<String> requestEntity = new HttpEntity<>(headers);

        try {
            ResponseEntity<String> responseEntity = restTemplate.exchange(
                    FASTAPI_SERVER_URL,
                    HttpMethod.POST,
                    requestEntity,
                    String.class
            );

            if (responseEntity.getStatusCode() == HttpStatus.OK) {
                String jsonResponseBody = responseEntity.getBody();
                ObjectMapper objectMapper = new ObjectMapper();
                List<Map<String, Object>> resultList = objectMapper.readValue(jsonResponseBody, new TypeReference<List<Map<String, Object>>>() {});
                model.addAttribute("htmlResponse", resultList);
            } else {
                // Handle unexpected status code
                model.addAttribute("error", "Unexpected status code: " + responseEntity.getStatusCode());
            }
        } catch (HttpServerErrorException e) {
            // Handle 5xx Server Errors
            model.addAttribute("error", "Internal Server Error: " + e.getRawStatusCode());
            e.printStackTrace();  // Log the exception
        } catch (Exception e) {
            // Handle other exceptions
            model.addAttribute("error", "An error occurred: " + e.getMessage());
            e.printStackTrace();  // Log the exception
        }

        return "/market/List";
    }
}
