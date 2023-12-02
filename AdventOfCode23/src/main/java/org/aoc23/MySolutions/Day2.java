package org.aoc23.MySolutions;

import org.aoc23.Helpers.MyFileReader;

import java.io.IOException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;

public class Day2 {
    private final String path = "/Users/glenn/repos/advent of code/AdventOfCode23/src/main/java/org/aoc23/Helpers/InputFiles/day2.txt";
    private final MyFileReader fReader = new MyFileReader(path);
    private final List<String> fileLines = fReader.readFile();

    public Day2() throws IOException {
    }

    public void part1() {
        final Map<String, Integer> max_cubes = new HashMap<>() {
            {
                put("red", 12);
                put("green", 13);
                put("blue", 14);
            }
        };
        int possibleCounter = 0;
        int gameCounter = 0;
        int sumOfGameNumbers = 0;
//        STRIP LEADING "Game x: " from each line
        for (int i = 0; i < fileLines.size(); i++) {
            String line = fileLines.get(i);
            line = line.replaceFirst("Game\\s\\d{1,2}:\\s", "");
            fileLines.set(i, line);
        }
//        For Each line:
        for (String line : fileLines) {
            boolean possible = true;
//        split into handfuls (semicolon)
            String[] handfuls = line.split("; ");
            for (String handful : handfuls) {
//        Check if any of the colours in each handful exceed the max
                String[] cubes = handful.split(", ");
                for (String cube : cubes) {
                    String[] cubeArray = cube.split(" ");
                    //                    Check red
                    if (Objects.equals(cubeArray[1], "red")) {
                        if (Integer.parseInt(cubeArray[0]) > max_cubes.get("red")) {
                            possible = false;
                        }
                        //                    Check blue
                    }
                    if (Objects.equals(cubeArray[1], "blue")) {
                        if (Integer.parseInt(cubeArray[0]) > max_cubes.get("blue")) {
                            possible = false;
                        }
                    }
                    //                    Check green
                    if (Objects.equals(cubeArray[1], "green")) {
                        if (Integer.parseInt(cubeArray[0]) > max_cubes.get("green")) {
                            possible = false;
                        }
                    }

                }
            }
            //        Else increase the possible counter
            if (possible) {
                possibleCounter++;
                sumOfGameNumbers += fileLines.indexOf(line) + 1;
            }
            gameCounter++;
        }
        System.out.println("Total games = " + gameCounter);
        System.out.println("Possible games = " + possibleCounter);
        System.out.println("Sum of game numbers = " + sumOfGameNumbers);
    }

    private void part2() {
        Integer sumOfPowers = 0;
        for (String line : fileLines) {
            int minGreen = 0;
            int minBlue = 0;
            int minRed = 0;

            String[] handfuls = line.split("; ");
            for (String handful : handfuls) {
                String[] cubes = handful.split(", ");
                for (String cube : cubes) {
                    String[] cubeArray = cube.split(" ");
                    if (Objects.equals(cubeArray[1], "red")) {
                        if (Integer.parseInt(cubeArray[0]) > minRed) {
                            minRed = Integer.parseInt(cubeArray[0]);
                        }
                    }
                    if (Objects.equals(cubeArray[1], "blue")) {
                        if (Integer.parseInt(cubeArray[0]) > minBlue) {
                            minBlue = Integer.parseInt(cubeArray[0]);
                        }
                    }
                    if (Objects.equals(cubeArray[1], "green")) {
                        if (Integer.parseInt(cubeArray[0]) > minGreen) {
                            minGreen = Integer.parseInt(cubeArray[0]);
                        }
                    }
                }
            }
            int powerOfSet = minBlue * minRed * minGreen;
            sumOfPowers += powerOfSet;
        }
        System.out.println("Sum of powers of all sets = " + sumOfPowers);
    }

    public static void main(String[] args) throws IOException {
        Day2 d2 = new Day2();
        d2.part1();
        d2.part2();
    }
}
