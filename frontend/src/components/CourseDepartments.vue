<template>
	<div class="text-ink-gray-7">
		<span v-if="requested_departments?.length == 1">
				{{ requested_departments[0].department_name }}
		</span>
		<span v-if="requested_departments?.length == 2">
				{{ requested_departments[0].department_name }}
			and
				{{ requested_departments[1].department_name }}
		</span>
		<span v-if="requested_departments?.length > 2">
				{{ requested_departments[0].department_name }}
			and {{ requested_departments?.length - 1 }} others
		</span>
	</div>
</template>
<script setup>
const props = defineProps({
	requested_departments: {
		type: Array,
		required: true,
	},
})
</script>
