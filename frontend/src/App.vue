<template>
  <div id="app">
    <GoalList />
  </div>
</template>

<script>
import GoalList from './components/GoalList.vue';
export default {
  name: 'App',
  components: { GoalList },
};
</script>
