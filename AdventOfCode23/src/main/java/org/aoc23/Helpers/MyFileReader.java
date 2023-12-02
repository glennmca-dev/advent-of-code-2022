package org.aoc23.Helpers;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class MyFileReader {
    private String filePath;
    private List<String> fileLines = new ArrayList<String>();
    public MyFileReader(String path){
        this.filePath = path;
    }

    public List<String> readFile() throws IOException {
        File file = new File(filePath);
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = br.readLine()) != null) {
                fileLines.add(line);
            }
            return fileLines;
        }
    }

}
