import * as Device from 'expo-device';
import { Platform, StyleSheet } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';

import { AnimatedIcon } from '@/components/animated-icon';
import { HintRow } from '@/components/hint-row';
import { ThemedText } from '@/components/themed-text';
import { ThemedView } from '@/components/themed-view';
import { WebBadge } from '@/components/web-badge';
import { BottomTabInset, MaxContentWidth, Spacing } from '@/constants/theme';



import React, { useState } from 'react';
import {
  View,
  Text,
  TouchableOpacity,
} from 'react-native';


export default function App() {
  const [display, setDisplay] = useState('0');
  const [firstValue, setFirstValue] = useState(null);
  const [operator, setOperator] = useState(null);
  const [newNumber, setNewNumber] = useState(true);

  const handlePress = (value) => {
    // Clear everything
    if (value === 'AC') {
      setDisplay('0');
      setFirstValue(null);
      setOperator(null);
      setNewNumber(true);
      return;
    }

    // Delete last digit
    if (value === 'DEL') {
      setDisplay((prev) =>
        prev.length <= 1 ? '0' : prev.slice(0, -1)
      );
      return;
    }

    // Select operator
    if (['+', '-', '×', '÷'].includes(value)) {
      setFirstValue(Number(display));
      setOperator(value);
      setNewNumber(true);
      return;
    }

    // Calculate result
    if (value === '=') {
      if (operator === null || firstValue === null) return;

      const secondValue = Number(display);
      let result;

      switch (operator) {
        case '+':
          result = firstValue + secondValue;
          break;

        case '-':
          result = firstValue - secondValue;
          break;

        case '×':
          result = firstValue * secondValue;
          break;

        case '÷':
          result =
            secondValue === 0
              ? 'Error'
              : firstValue / secondValue;
          break;

        default:
          return;
      }

      setDisplay(
        typeof result === 'number' && Number.isFinite(result)
          ? String(Number(result.toFixed(8)))
          : String(result)
      );

      setFirstValue(null);
      setOperator(null);
      setNewNumber(true);
      return;
    }

    // Enter decimal point
    if (value === '.') {
      if (newNumber) {
        setDisplay('0.');
        setNewNumber(false);
      } else if (!display.includes('.')) {
        setDisplay(display + '.');
      }
      return;
    }

    // Enter digits
    if (newNumber || display === '0' || display === 'Error') {
      setDisplay(value);
      setNewNumber(false);
    } else {
      setDisplay(display + value);
    }
  };

  const buttons = [
    ['AC', 'DEL', '÷'],
    ['7', '8', '9', '×'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '='],
  ];

  const renderButton = (value) => {
    const isOperator = ['+', '-', '×', '÷', '='].includes(value);
    const isUtility = ['AC', 'DEL'].includes(value);

    return (
      <TouchableOpacity
        key={value}
        style={[
          styles.button,
          value === '0' && styles.zeroButton,
          isOperator && styles.operatorButton,
          isUtility && styles.utilityButton,
        ]}
        onPress={() => handlePress(value)}
        activeOpacity={0.7}
      >
        <Text
          style={[
            styles.buttonText,
            isOperator && styles.operatorText,
            isUtility && styles.utilityText,
          ]}
        >
          {value}
        </Text>
      </TouchableOpacity>
    );
  };

  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.heading}>Calculator</Text>

      <View style={styles.displayContainer}>
        <Text
          style={styles.display}
          numberOfLines={1}
          adjustsFontSizeToFit
        >
          {display}
        </Text>
      </View>

      <View style={styles.keypad}>
        {buttons.map((row, index) => (
          <View style={styles.row} key={index}>
            {row.map(renderButton)}
          </View>
        ))}
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'white',
    padding: 20,
    justifyContent: 'center',
  },

  heading: {
    color: 'black',
    fontSize: 28,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 20,
  },

  displayContainer: {
    minHeight: 100,
    justifyContent: 'flex-end',
    alignItems: 'flex-end',
    backgroundColor: 'lightgray',
    borderRadius: 8,
    padding: 15,
    marginBottom: 15,
  },

  display: {
    color: 'black',
    fontSize: 40,
  },

  keypad: {
    gap: 8,
  },

  row: {
    flexDirection: 'row',
    gap: 8,
  },

  button: {
    flex: 1,
    height: 60,
    backgroundColor: 'lightgray',
    borderRadius: 8,
    justifyContent: 'center',
    alignItems: 'center',
  },

  zeroButton: {
    flex: 2,
  },

  operatorButton: {
    backgroundColor: 'lightblue',
  },

  utilityButton: {
    backgroundColor: 'silver',
  },

  buttonText: {
    color: 'black',
    fontSize: 22,
  },

  operatorText: {
    color: 'black',
    fontWeight: 'bold',
  },

  utilityText: {
    color: 'black',
  },
});
