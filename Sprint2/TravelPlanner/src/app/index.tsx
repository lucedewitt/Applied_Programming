// import * as Device from 'expo-device';
import React, { useState } from 'react';
import {
  View,
  Text,
  Image,
  Modal,
  Pressable,
  ScrollView,
  TextInput,
  StyleSheet,
} from 'react-native';
import { Calendar } from 'react-native-calendars';
// import { SafeAreaView } from 'react-native-safe-area-context';

// import { AnimatedIcon } from '@/components/animated-icon';
// import { HintRow } from '@/components/hint-row';
// import { ThemedText } from '@/components/themed-text';
// import { ThemedView } from '@/components/themed-view';
// import { WebBadge } from '@/components/web-badge';
// import { BottomTabInset, MaxContentWidth, Spacing } from '@/constants/theme';

const initialEvents = [
  {
    id: '1',
    date: '2026-10-15',
    title: 'Doctor appointment',
    time: '10:00 AM',
  },
  {
    id: '2',
    date: '2026-10-15',
    title: 'Team meeting',
    time: '2:00 PM',
  },
  {
    id: '3',
    date: '2026-10-20',
    title: 'Project deadline',
    time: 'All day',
  },
];

export default function HomeScreen() {
  const [events, setEvents] = useState(initialEvents);
  const [selectedDate, setSelectedDate] = useState('2026-10-15');
  const [modalVisible, setModalVisible] = useState(false);
  const [editingDay, setEditingDay] = useState(false);
  const [newEventTitle, setNewEventTitle] = useState('');
  const [newEventTime, setNewEventTime] = useState('');
  const selectedEvents = events.filter(event => event.date === selectedDate);
  const markedDates: Record<string, any> = {};

  const formattedSelectedDate = (() => {
    const [year, month, day] = selectedDate.split('-').map(Number);
    return new Date(year, month - 1, day).toLocaleDateString('en-US', {
      month: 'long',
      day: 'numeric',
      year: 'numeric',
    });
  })();

  const addEvent = () => {
    if (!newEventTitle.trim()) return;

    setEvents(currentEvents => [
      ...currentEvents,
      {
        id: Date.now().toString(),
        date: selectedDate,
        title: newEventTitle.trim(),
        time: newEventTime.trim() || 'All day',
      },
    ]);
    setNewEventTitle('');
    setNewEventTime('');
  };

  const updateEvent = (id: string, field: 'title' | 'time', value: string) => {
    setEvents(currentEvents =>
      currentEvents.map(event =>
        event.id === id ? { ...event, [field]: value } : event
      )
    );
  };

  const deleteEvent = (id: string) => {
    setEvents(currentEvents => currentEvents.filter(event => event.id !== id));
  };

  events.forEach(event => {
    markedDates[event.date] = {
      marked: true,
      dotColor: '#194454',
    };
  });

  markedDates[selectedDate] = {
    ...markedDates[selectedDate],
    selected: true,
    selectedColor: '#995C54',
  };

  return (
    <View style={{ flex: 1 }}>
      {/* Header */}
      <View style={styles.header}>
        <View style={styles.headerContent}>
          <View style={styles.logoBackground}>
            <Image
              source={require('../../assets/images/appIcon120.png')}
              style={styles.logo} resizeMode="contain"
            />
          </View>
          <Text style={styles.title}>Travel Planner</Text>
        </View>
      </View>

      {/* Calendar */}
      <View style={styles.container}>
        <Calendar
          onDayPress={day => {
            setSelectedDate(day.dateString);
            setModalVisible(true);
          }}
          markedDates={markedDates}
        />
      </View>

      <Modal
        visible={modalVisible}
        transparent
        animationType="fade"
        onRequestClose={() => setModalVisible(false)}
      >
        <View style={styles.modalOverlay}>
          <View style={styles.modalContent}>
            <Text style={styles.modalTitle}>
              Events on {formattedSelectedDate}
            </Text>

            <ScrollView>
              {selectedEvents.length === 0 && (
                <Text>No events for this day.</Text>
              )}

              {selectedEvents.map(item => (
                <View style={styles.event} key={item.id}>
                  {editingDay ? (
                    <>
                      <TextInput
                        style={styles.input}
                        value={item.title}
                        onChangeText={value => updateEvent(item.id, 'title', value)}
                        placeholder="Event title"
                      />
                      <TextInput
                        style={styles.input}
                        value={item.time}
                        onChangeText={value => updateEvent(item.id, 'time', value)}
                        placeholder="Time"
                      />
                      <Pressable
                        style={styles.deleteButton}
                        onPress={() => deleteEvent(item.id)}
                      >
                        <Text style={styles.deleteButtonText}>Delete event</Text>
                      </Pressable>
                    </>
                  ) : (
                    <>
                      <Text style={styles.titleC}>{item.title}</Text>
                      <Text>{item.time}</Text>
                    </>
                  )}
                </View>
              ))}

              {editingDay && (
                <View style={styles.addEventSection}>
                  <Text style={styles.sectionTitle}>Add event</Text>
                  <TextInput
                    style={styles.input}
                    value={newEventTitle}
                    onChangeText={setNewEventTitle}
                    placeholder="Event title"
                  />
                  <TextInput
                    style={styles.input}
                    value={newEventTime}
                    onChangeText={setNewEventTime}
                    placeholder="Time (optional)"
                  />
                  <Pressable style={styles.addButton} onPress={addEvent}>
                    <Text style={styles.buttonText}>Add event</Text>
                  </Pressable>
                </View>
              )}
            </ScrollView>

            <View style={styles.buttonRow}>
              <Pressable
                style={styles.editButton}
                onPress={() => setEditingDay(currentValue => !currentValue)}
              >
                <Text style={styles.buttonText}>
                  {editingDay ? 'Done editing' : 'Edit day'}
                </Text>
              </Pressable>

              <Pressable
                style={styles.closeButton}
                onPress={() => {
                  setModalVisible(false);
                  setEditingDay(false);
                }}
              >
                <Text style={styles.closeButtonText}>Close</Text>
              </Pressable>
            </View>
          </View>
        </View>
      </Modal>
    </View>
  );
}

const styles = StyleSheet.create({
  header: {
    height: 100,
    backgroundColor: '#DA6555',
    // height: 64,
    // paddingHorizontal: 16,
    // flexDirection: 'row',
    // alignItems: 'center',
    // backgroundColor: '#FFFFFF',
    // borderBottomWidth: 1,
    // borderBottomColor: '#e5e5e5',
  },
  headerContent: {
    marginTop: 50,
    paddingHorizontal: 16,
    flexDirection: 'row',
    alignItems: 'center',
  },
  logoBackground: {
    height: 35,
    width: 36,
    backgroundColor: '#41B8AA',
    marginRight: 12,
    borderRadius: 10,
  },
  logo: {
    width: 60,
    height: 60,
    // transform: [
    //   { translateX: -12}, // right
    //   { translateY: -16}, // down
    // ],
    position: 'relative',
    right: 12,
    bottom: 16,
  },
  title: {
    fontSize: 22,
    fontWeight: 'bold',
    color: '#222222',
  },

  container: {
    flex: 1,
    padding: 16,
  },
  event: {
    padding: 16,
    marginTop: 10,
    backgroundColor: '#eeeeee',
    borderRadius: 8,
  },
  titleC: {
    fontSize: 16,
    fontWeight: 'bold',
  },
  input: {
    marginBottom: 8,
    padding: 10,
    backgroundColor: '#ffffff',
    borderWidth: 1,
    borderColor: '#cccccc',
    borderRadius: 6,
  },
  addEventSection: {
    marginTop: 16,
    paddingTop: 12,
    borderTopWidth: 1,
    borderTopColor: '#dddddd',
  },
  sectionTitle: {
    marginBottom: 8,
    fontSize: 16,
    fontWeight: 'bold',
  },
  editButton: {
    flex: 1,
    padding: 12,
    alignItems: 'center',
    backgroundColor: '#41B8AA',
    borderRadius: 8,
  },
  buttonRow: {
    flexDirection: 'row',
    gap: 10,
    marginTop: 16,
  },
  addButton: {
    alignSelf: 'flex-start',
    paddingHorizontal: 14,
    paddingVertical: 10,
    backgroundColor: '#194454',
    borderRadius: 8,
  },
  deleteButton: {
    alignSelf: 'flex-start',
    marginTop: 4,
    paddingHorizontal: 12,
    paddingVertical: 8,
    backgroundColor: '#d9534f',
    borderRadius: 6,
  },
  deleteButtonText: {
    color: '#ffffff',
    fontWeight: 'bold',
  },
  buttonText: {
    color: '#ffffff',
    fontWeight: 'bold',
  },
  modalOverlay: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'rgba(0, 0, 0, 0.45)',
  },
  modalContent: {
    width: '85%',
    maxHeight: '70%',
    padding: 20,
    backgroundColor: '#ffffff',
    borderRadius: 16,
  },
  modalTitle: {
    marginBottom: 10,
    fontSize: 20,
    fontWeight: 'bold',
  },
  closeButton: {
    flex: 1,
    padding: 12,
    alignItems: 'center',
    backgroundColor: '#194454',
    borderRadius: 8,
  },
  closeButtonText: {
    color: '#ffffff',
    fontWeight: 'bold',
  },
});

// function getDevMenuHint() {
//   if (Platform.OS === 'web') {
//     return <ThemedText type="small">use browser devtools</ThemedText>;
//   }
//   if (Device.isDevice) {
//     return (
//       <ThemedText type="small">
//         shake device or press <ThemedText type="code">m</ThemedText> in terminal
//       </ThemedText>
//     );
//   }
//   const shortcut = Platform.OS === 'android' ? 'cmd+m (or ctrl+m)' : 'cmd+d';
//   return (
//     <ThemedText type="small">
//       press <ThemedText type="code">{shortcut}</ThemedText>
//     </ThemedText>
//   );
// }

// export default function HomeScreen() {
//   return (
//     <ThemedView style={styles.container}>
//       <SafeAreaView style={styles.safeArea}>
//         <ThemedView style={styles.heroSection}>
//           {/* <AnimatedIcon /> */}
//           <Image source={require("../../assets/images/appIcon120.png")} style={styles.image} />
//           <ThemedText type="title" style={styles.title}>
//             Welcome to&nbsp;Expo
//           </ThemedText>
//         </ThemedView>

//         <ThemedText type="code" style={styles.code}>
//           get started
//         </ThemedText>

//         <ThemedView type="backgroundElement" style={styles.stepContainer}>
//           <HintRow
//             title="Try editing"
//             hint={<ThemedText type="code">src/app/index.tsx</ThemedText>}
//           />
//           <HintRow title="Dev tools" hint={getDevMenuHint()} />
//           <HintRow
//             title="Fresh start"
//             hint={<ThemedText type="code">npm run reset-project</ThemedText>}
//           />
//         </ThemedView>

//         {Platform.OS === 'web' && <WebBadge />}
//       </SafeAreaView>
//     </ThemedView>
//   );
// }

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     justifyContent: 'center',
//     flexDirection: 'row',
//   },
//   safeArea: {
//     flex: 1,
//     paddingHorizontal: Spacing.four,
//     alignItems: 'center',
//     gap: Spacing.three,
//     paddingBottom: BottomTabInset + Spacing.three,
//     maxWidth: MaxContentWidth,
//   },
//   heroSection: {
//     alignItems: 'center',
//     justifyContent: 'center',
//     flex: 1,
//     paddingHorizontal: Spacing.four,
//     gap: Spacing.four,
//   },
//   title: {
//     textAlign: 'center',
//   },
//   code: {
//     textTransform: 'uppercase',
//   },
//   stepContainer: {
//     gap: Spacing.three,
//     alignSelf: 'stretch',
//     paddingHorizontal: Spacing.three,
//     paddingVertical: Spacing.four,
//     borderRadius: Spacing.four,
//   },

//   image: {
//     width: 300,
//     height: 200,
//     resizeMode: "cover",
//   },
// });
