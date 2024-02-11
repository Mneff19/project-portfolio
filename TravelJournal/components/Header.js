import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

const Header = () => {
  return (
    <View style={styles.header}>
        <Text style={styles.text}>Travel Journal</Text>
    </View>
  );
}

const styles = StyleSheet.create({
    header: {
        paddingTop: 60,
        paddingLeft: 15,
        paddingRight: 15,
        paddingBottom: 30,
        marginBottom: 40,
        backgroundColor: '#2b2d42'
    },
    text: {
        textAlign: 'center',
        color: '#edf2f4',
        fontSize: 24,
        fontWeight: '700',
    }
});


export default Header;
