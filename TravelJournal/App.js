import React, { useState } from 'react';
import { StyleSheet, Alert } from 'react-native';
import Header from './components/Header';
import AddEntry from './components/AddEntry';
import Entry from './components/Entry';
import 'react-native-get-random-values';
import { KeyboardAwareFlatList } from 'react-native-keyboard-aware-scroll-view';
import { uuid } from 'uuidv4';

const App = () => {
  const [entries, setEntries] = useState([
    // {
    //   id: uuid(),
    //   url: "https://picsum.photos/300/300",
    //   note: "Lorem ipsum dolor sit alrbe sofs vsosf volor dolor bolor tolor"
    // },
  ]);

  const deleteEntry = (id) => {
    setEntries(prevEntries => {
      return prevEntries.filter(item => item.id !== id);
    });
  };

  const addEntry = (atts) => {
    if (!atts[1]) {
      Alert.alert(
          'No text entered',
          'Please enter text when adding your entry',
          [
              {
                  text: 'Understood',
                  style: 'cancel',
              },
          ],
          {cancelable: true},
      );
      return;

    } else if (!atts[0]) {
        Alert.alert(
            'No image selected',
            'Please select an image when adding your entry',
            [
                {
                    text: 'Understood',
                    style: 'cancel',
                },
            ],
            {cancelable: true},
        );
        return;
    }
    setEntries(prevEntries => {
      return [...prevEntries, {id: uuid(), url: atts[0], note: atts[1]}];
    });
  };

  const renderHeader = () => {
    return <Header />;
  }

  const renderAddEntry = () => {
    return <AddEntry addEntry={addEntry} />;
  }

  return (
    <>
    <KeyboardAwareFlatList
      ListHeaderComponent={renderHeader}
      stickyHeaderIndices={[0]}
      ListFooterComponent={renderAddEntry}
      style={styles.list}
      data={entries}
      renderItem={(entry) => 
        <Entry
        entry={entry}
        deleteEntry={deleteEntry} />
      }
    />
    {/* <ImagePickerExample/> */}
    </>
  );
};

const styles = StyleSheet.create({
  list: {
    flex: 1,
    backgroundColor: "#edf2f4"
  }
});


export default App;
