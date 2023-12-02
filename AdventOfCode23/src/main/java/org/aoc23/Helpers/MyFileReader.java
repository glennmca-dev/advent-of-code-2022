package org.aoc23.Helpers;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class MyFileReader{
    private final String filePath;
    private List<String> fileLines = new ArrayList<>();
    public MyFileReader(String path) throws FileNotFoundException {
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
        } catch (FileNotFoundException e) {
            throw new FileNotFoundException(e.toString());
        }
    }

}
