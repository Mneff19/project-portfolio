import React from 'react';
import { StyleSheet, Text, View, Image, TouchableOpacity } from 'react-native';

const Entry = ({entry, deleteEntry}) => {
  return (
    <View style={styles.entry}>
        <Image style={styles.image} source={{
            uri: entry.item.url
        }} />
        <Text style={styles.text}>{entry.item.note}</Text>
        <TouchableOpacity onPress={() => {deleteEntry(entry.item.id)}}>
            <Text style={styles.close}>Remove Entry</Text>
        </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
    entry: {
        padding: 30,
        marginLeft: 25,
        marginRight: 25,
        marginBottom: 25,
        borderColor: '#2b2d42',
        borderWidth: 2,
        borderRadius: 8,
        backgroundColor: 'white'
    },
    text: {
        fontSize: 18,
        color: "black"
    },
    image: {
        width: 250,
        height: 250,
        marginBottom: 20,
        marginLeft: "auto",
        marginRight: "auto"
    },
    close: {
        fontSize: 16,
        fontWeight: "600",
        color: "#d90429",
        textAlign: "center",
        marginTop: 20
    }
});


export default Entry;
