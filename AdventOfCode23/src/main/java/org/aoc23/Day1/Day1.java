package org.aoc23.Day1;

import org.aoc23.Helpers.MyFileReader;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Day1 {
    private final String path = "src/main/resources/InputFiles/day1.txt";
    private final MyFileReader fReader = new MyFileReader(path);
    private final List<String> fileLines = fReader.readFile();

    public Day1() throws IOException {
    }

    public void part1() throws IOException {
        List<Integer> numbers = new ArrayList<>();

        for (String line : fileLines) {
            Character firstNumChar = null;
            Character lastNumChar = null;
            for (char lineChar : line.toCharArray()) {
                if(Character.isDigit(lineChar) && firstNumChar == null){
                    firstNumChar = lineChar;
                } else if (Character.isDigit(lineChar) && firstNumChar != null) {
                    lastNumChar = lineChar;
                }
            }
            if(lastNumChar != null){
                char[] charnums = {firstNumChar, lastNumChar};
                String charResult = new String(charnums);
                numbers.add(Integer.parseInt(charResult));
            }
            if(lastNumChar == null){
                char[] charnums = {firstNumChar, firstNumChar};
                String charResult = new String(charnums);
                numbers.add(Integer.parseInt(charResult));
            }
        }
        Integer total = 0;
        for(Integer num : numbers){
            total += num;
        }
        System.out.println("Number List Total (puzzle Answer):");
        System.out.println(total);
    }

    public void part2() {
        List<Integer> numbers = new ArrayList<>();
        String[] nums = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        String[] replacements = {"one1e", "two2o", "three3e", "four4r", "five5e", "six6x", "seven7n", "eight8t", "nine9e"};
        for (int i = 0; i < fileLines.size(); i++){
            for (int j = 0; j< nums.length; j++) {
                String line = fileLines.get(i).replace(nums[j], replacements[j]);
                fileLines.set(i, line);
                }
                String compare= fileLines.get(i);
                System.out.println(compare);
            }
        }

    public static void main(String[] args) throws IOException {
        Day1 d1 = new Day1();
        System.out.println("Running Part 1");
        System.out.println("Part 1 \n=========================");
        d1.part1();
        System.out.println("\n=========================\nRunning Part 2");
        System.out.println("Part 2 \n=========================");
        d1.part2();
        d1.part1();
    }
}

