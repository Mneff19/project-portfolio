import React, {useState} from 'react';
import { StyleSheet, Text, TextInput, View, Image, TouchableOpacity } from 'react-native';
import * as ImagePicker from 'expo-image-picker';

const AddEntry = ({addEntry}) => {
    const [url, setURL] = useState(null);
    const [note, setNote] = useState("");
  
    const pickImage = async () => {
      // No permissions request is necessary for launching the image library
      let result = await ImagePicker.launchImageLibraryAsync({
        mediaTypes: ImagePicker.MediaTypeOptions.All,
        allowsEditing: true,
        aspect: [4, 3],
        quality: 1,
      });
  
      if (!result.canceled) {
        setURL(result.assets[0].uri);
      }
    };

    const onChangeNote = textVal => {
        setNote(textVal);
    }

    return (
        <View style={styles.container}>
            <TouchableOpacity style={styles.addImage} onPress={pickImage}>
                {!url && <Text style={styles.addImageText}>Pick an image from camera roll</Text>}
                {url && <Image style={styles.image} source={{
                    url: url
                }} /> }
            </TouchableOpacity>
            <TextInput
                placeholder="Add note here..."
                style={styles.text}
                onChangeText={onChangeNote}
                value={note}
             />
            <TouchableOpacity onPress={() => {addEntry([url, note])}}>
                <Text style={styles.close}>Add Entry</Text>
            </TouchableOpacity>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
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
    addImage: {
        width: 250,
        height: 250,
        marginBottom: 20,
        marginLeft: "auto",
        marginRight: "auto",
        justifyContent: "center"
    },
    image: {
        width: 250,
        height: 250
    },
    addImageText: {
        fontSize: 24,
        fontWeight: "500",
        textAlign: "center",
        color: "#2b2d42"
    },
    close: {
        fontSize: 16,
        fontWeight: "600",
        color: "#2F843F",
        textAlign: "center",
        marginTop: 20
    }
});


export default AddEntry;
