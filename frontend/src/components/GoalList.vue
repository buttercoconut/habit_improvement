<template>
  <div>
    <h2>Goal List</h2>
    <ul>
      <li v-for="goal in goals" :key="goal.id">
        {{ goal.title }} - {{ goal.progress }}%
      </li>
    </ul>
  </div>
</template>

<script>
import { fetchGoals } from '../api/goal';
export default {
  name: 'GoalList',
  data() {
    return {
      goals: [],
    };
  },
  async created() {
    const userId = 1; // placeholder
    this.goals = await fetchGoals(userId);
  },
};
</script>
